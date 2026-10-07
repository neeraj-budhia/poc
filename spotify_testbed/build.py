#!/usr/bin/env python3
"""Build the Spotify-style web localization testbed.

Renders HTML screens (screens/*.html) with per-locale strings (strings/<code>.json)
in headless Chromium, plants DOM/CSS defects from cases.yml into the target render,
and writes one case folder per variant in the same layout as the Android case packs
(~/Downloads/android/<lang>/<ID>/):

  annotated/base.jpg, target.jpg   numbered boxes burned in (same number = same element)
  source/base.png, target.png      raw screenshots (1080x2400 = 360x800 CSS px @3x)
  source/base.html, target.html    rendered DOM (the web analogue of uiautomator XML)
  verify/report.json               per-defect check that the plant actually rendered
  verify/element-*.png             crops of each planted element, both locales
  case.json, CASE.md, mapping.json, request.json

Usage: .venv/bin/python spotify_testbed/build.py [--out DIR] [CASE_ID ...]
"""
import argparse
import json
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from locales import LOCALES, RTL_CODES  # noqa: E402

BASE_CODE = "en-US"
VIEWPORT = {"width": 360, "height": 800}
DPR = 3
TREE_SPACE = [VIEWPORT["width"] * DPR, VIEWPORT["height"] * DPR]
ANNOT_WIDTH = 768
BOX_COLOR = (236, 64, 152)
DEFAULT_OUT = HERE.parent / "dataset/spotify_web_v4"

# Fills strings, plants defects, returns every visible text element with its box.
# String-layer defects arrive as d.text; CSS-layer defects as d.op and are sized from the
# element's own measured box so they fit any script (a fixed px width would not).
RENDER_JS = """
([strings, defects, lang, dir]) => {
  document.documentElement.lang = lang;
  document.documentElement.dir = dir;
  for (const el of document.querySelectorAll('[data-k]')) {
    const k = el.dataset.k;
    el.textContent = k in strings ? strings[k] : k;
    // RTL UIs isolate Latin-only strings (names, titles, times) so bidi doesn't flip their punctuation
    if (dir === 'rtl' && !/[\u0590-\u08FF\uFB1D-\uFEFF]/.test(el.textContent)) {
      el.style.cssText += ';direction:ltr;unicode-bidi:isolate';
      if (getComputedStyle(el).display === 'block') el.style.textAlign = 'right';
    }
    // Nastaliq is very tall: real Urdu UIs open up the line height of Urdu text
    if (lang === 'ur' && /[\u0600-\u06FF]/.test(el.textContent)) el.style.lineHeight = '1.9';
  }
  // natural single-line width: measured after forcing one line, else block elements report the container width
  const natural = el => {
    el.style.cssText += ';display:inline-block;white-space:nowrap;max-width:none;vertical-align:bottom';
    return el.getBoundingClientRect().width;
  };
  const textEls = () => [...document.querySelectorAll('[data-k]')];
  const OPS = {
    clip_h: (el, r) => { const w = natural(el); el.style.cssText += `;overflow:hidden;width:${Math.round(w * 0.55)}px`; },
    ellipsis: (el, r) => { const w = natural(el); el.style.cssText += `;overflow:hidden;text-overflow:ellipsis;max-width:${Math.round(w * 0.55)}px`; },
    clip_v: (el, r) => {
      // sized from font-size, not line height: tall scripts (Nastaliq, Tamil) have big line boxes
      const h = Math.round(parseFloat(getComputedStyle(el).fontSize) * 0.6);
      el.style.cssText += `;display:inline-block;white-space:nowrap;overflow:hidden;height:${h}px;line-height:${h}px`;
    },
    overlap: (el, r) => {
      // pull the element up onto the nearest text element above it that shares horizontal space
      const above = textEls().filter(o => o !== el).map(o => o.getBoundingClientRect())
        .filter(o => o.bottom <= r.top + 1 && Math.min(o.right, r.right) - Math.max(o.left, r.left) > 8)
        .sort((a, b) => b.bottom - a.bottom)[0];
      const dy = above ? r.top - (above.top + above.height * 0.35) : Math.max(r.height, 14) * 0.8;
      el.style.cssText += `;position:relative;top:-${Math.round(dy)}px`;
    },
    offscreen: (el, r) => {
      // push 40% of the text past the screen edge it reads towards
      const w = natural(el), b = el.getBoundingClientRect();
      const dx = dir === 'rtl' ? (w * 0.4) - b.right : (window.innerWidth - w * 0.6) - b.left;
      el.style.cssText += `;transform:translateX(${Math.round(dx)}px)`;
    },
    rtl_ltr: (el, r) => { el.setAttribute('dir', 'ltr'); el.style.cssText += ';display:block;direction:ltr;text-align:left'; },
  };
  for (const d of defects) {
    const el = document.querySelector(`[data-k="${d.element}"]`);
    if (!el) throw new Error('defect element not on screen: ' + d.element);
    if (d.text !== undefined && d.text !== null) el.textContent = d.text;
    if (d.op) {
      if (!OPS[d.op]) throw new Error('unknown op ' + d.op);
      OPS[d.op](el, el.getBoundingClientRect());
    }
  }
  // only text fully on screen (and not hidden under the tab bar) is sent
  const tabbar = document.querySelector('.tabbar');
  const fold = tabbar ? tabbar.getBoundingClientRect().top : window.innerHeight;
  return [...document.querySelectorAll('[data-k]')].map(el => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const bottomLimit = tabbar && tabbar.contains(el) ? window.innerHeight : fold;
    return {
      key: el.dataset.k, text: el.textContent.trim(),
      box: [r.left, r.top, r.right, r.bottom],
      visible: r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && r.top >= 0 && r.bottom <= bottomLimit + 1,
      clipped: el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1,
      direction: cs.direction, text_align: cs.textAlign, font_size: parseFloat(cs.fontSize),
      content_h: el.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom),
    };
  });
}
"""


def target_lang_label(code):
    name = LOCALES[code][0].split(" (")[0] if code in LOCALES else "English"
    return f"{name} ({code})"


def render(page, screen, code, defects):
    strings = json.loads((HERE / "strings" / f"{code}.json").read_text())
    page.goto((HERE / "screens" / f"{screen}.html").as_uri())
    direction = "rtl" if code in RTL_CODES else "ltr"
    elements = page.evaluate(RENDER_JS, [strings, defects, code, direction])
    return elements, page.screenshot(), page.content()


def px_box(box):
    x0, y0, x1, y1 = (round(v * DPR) for v in box)
    w, h = TREE_SPACE
    return [min(max(x0, 0), w), min(max(y0, 0), h), min(max(x1, 0), w), min(max(y1, 0), h)]


def overlap_ratio(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    area = max(min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1])), 1)
    return ix * iy / area


def pct_box(box):
    x0, y0, x1, y1 = box
    w, h = TREE_SPACE
    return {"x": round(x0 / w * 100, 3), "y": round(y0 / h * 100, 3),
            "width": round((x1 - x0) / w * 100, 3), "height": round((y1 - y0) / h * 100, 3)}


def annotate(png_path, boxes, out_path):
    img = Image.open(png_path).convert("RGB")
    scale = ANNOT_WIDTH / img.width
    img = img.resize((ANNOT_WIDTH, round(img.height * scale)), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=9)
    for num, box in boxes.items():
        x0, y0, x1, y1 = (round(v * scale) for v in box)
        draw.rectangle([x0, y0, x1, y1], outline=BOX_COLOR, width=2)
        tw = draw.textlength(num, font=font)
        draw.rectangle([x0, y0 - 11, x0 + tw + 4, y0], fill=BOX_COLOR)
        draw.text((x0 + 2, y0 - 11), num, fill="white", font=font)
    img.save(out_path, quality=90)
    return img.size


def verify_defect(defect, key, target_els, base_el):
    tgt_el = target_els[key]
    check = defect["check"]
    if check == "text":
        ok = tgt_el["text"] == defect["text"].strip()
        why = "target renders the planted string" if ok else f"target renders {tgt_el['text']!r}"
    elif check == "clipped":
        ok = tgt_el["clipped"]
        why = "element content overflows its box (scroll > client)" if ok else "no overflow measured"
    elif check == "clipped_v":
        h = tgt_el["content_h"]
        ok = h < 0.9 * tgt_el["font_size"]
        why = f"line box {h:.0f}px < font-size {tgt_el['font_size']:.0f}px, glyph tops/bottoms cut"
    elif check == "direction":
        ok = tgt_el["direction"] == "ltr" and tgt_el["text_align"] in ("left", "start")
        why = f"direction={tgt_el['direction']} text-align={tgt_el['text_align']} inside rtl page"
    elif check == "overlap":
        hits = [k for k, e in target_els.items()
                if k != key and e["visible"] and overlap_ratio(tgt_el["box"], e["box"]) > 0.15]
        ok = bool(hits)
        why = f"overlaps {hits}" if ok else "no overlap with another text element"
    elif check == "offscreen":
        x0, _, x1, _ = tgt_el["box"]
        ok = x1 > VIEWPORT["width"] + 1 or x0 < -1
        why = f"text box x=[{x0:.0f},{x1:.0f}] extends past the {VIEWPORT['width']}px screen edge"
    else:
        raise ValueError(f"unknown check {check!r}")
    return {"element_id": key, "subcategory": defect["subcategory"],
            "verdict": "present" if ok else "absent", "why": why,
            "base_text": base_el["text"], "target_text": tgt_el["text"]}


def crop(png_path, box, out_path, pad=24):
    img = Image.open(png_path)
    x0, y0, x1, y1 = box
    img.crop((max(x0 - pad, 0), max(y0 - pad, 0),
              min(x1 + pad, img.width), min(y1 + pad, img.height))).save(out_path)


def build_case(page, case, out_root):
    cid, code, screen = case["id"], case["lang"], case["screen"]
    case_dir = out_root / code / cid
    for sub in ("annotated", "source", "verify"):
        (case_dir / sub).mkdir(parents=True, exist_ok=True)

    shots = {}
    for side, lang_code, defects in (("base", BASE_CODE, []), ("target", code, case["defects"])):
        els, png, html = render(page, screen, lang_code, defects)
        (case_dir / "source" / f"{side}.png").write_bytes(png)
        (case_dir / "source" / f"{side}.html").write_text(html)
        shots[side] = {e["key"]: e for e in els}

    # sent = text visible in both locales (tall scripts can push rows below the fold)
    keys = [k for k, e in shots["base"].items()
            if e["visible"] and e["text"] and shots["target"][k]["visible"]]
    off = [d["element"] for d in case["defects"] if d["element"] not in keys]
    if off:
        raise ValueError(f"{cid}: planted element(s) not on screen in both locales: {off}")
    excluded = len(shots["base"]) - len(keys)
    num_of = {k: str(i) for i, k in enumerate(keys, 1)}
    elements = [{
        "id": num_of[k], "element_id": k, "descriptor": shots["base"][k]["text"],
        "target_text": shots["target"][k]["text"],
        "base_box": px_box(shots["base"][k]["box"]), "target_box": px_box(shots["target"][k]["box"]),
        "status": "matched", "match_method": "stable_id",
    } for k in keys]

    images = {}
    for side in ("base", "target"):
        boxes = {e["id"]: e[f"{side}_box"] for e in elements}
        w, h = annotate(case_dir / "source" / f"{side}.png", boxes, case_dir / "annotated" / f"{side}.jpg")
        images[side] = {"file": f"annotated/{side}.jpg", "width": w, "height": h, "tree_space": TREE_SPACE}

    case_elements = [{"box": num_of[d["element"]], "element_id": d["element"], "resolved_by": "planted"}
                     for d in case["defects"]]
    target_lang = target_lang_label(code)
    mapping = {
        "case_id": cid, "screen": screen, "corpus": "spotify_web (rendered)",
        "base_lang": target_lang_label(BASE_CODE), "target_lang": target_lang,
        "case_elements": case_elements, "base_image": images["base"], "target_image": images["target"],
        "counts": {"elements_sent": len(elements), "with_target_box": len(elements),
                   "excluded_no_visible_text": excluded, "target_only_not_sent": 0},
        "elements": elements, "target_only_elements": [],
        "base_bounding_boxes": {e["id"]: pct_box(e["base_box"]) for e in elements},
        "target_bounding_boxes": {e["id"]: pct_box(e["target_box"]) for e in elements},
    }
    request = {
        "product": "app-lca", "workflow": "localization-check", "client_ref": f"{cid}:{screen}",
        "attachment_ids": ["<source/base.png>", "<source/target.png>"],
        "payload": {
            "base_lang": mapping["base_lang"], "target_lang": target_lang, "tree_space": TREE_SPACE,
            "elements": {e["element_id"]: {"desc": e["descriptor"], "bbox_base": e["base_box"],
                                           "bbox_head": e["target_box"], "text_head": e["target_text"],
                                           "match": e["match_method"]} for e in elements},
        },
    }
    checks = [verify_defect(d, d["element"], shots["target"], shots["base"][d["element"]])
              for d in case["defects"]]
    for d, cel in zip(case["defects"], case_elements):
        n = cel["box"]
        crop(case_dir / "source/base.png", px_box(shots["base"][d["element"]]["box"]),
             case_dir / "verify" / f"element-{n}-base.png")
        crop(case_dir / "source/target.png", px_box(shots["target"][d["element"]]["box"]),
             case_dir / "verify" / f"element-{n}-target.png")
    verdict = ("control" if not checks else
               "present" if all(c["verdict"] == "present" for c in checks) else "partial")
    report = {"case_id": cid, "language": code, "screen": screen, "verdict": verdict,
              "defects": [{"box": c["box"], **chk} for c, chk in zip(case_elements, checks)]}
    # brand / do-not-translate strings: identical in both locales and NOT a defect (FP probes)
    dnt = [num_of[k] for k in keys if shots["target"][k]["text"] == shots["base"][k]["text"]
           and k not in {d["element"] for d in case["defects"]}]
    case_json = {"case_id": cid, "platform": "web", "language": code, "screen": screen,
                 "is_control": not case["defects"], "do_not_translate_boxes": dnt,
                 "defects": [{"box": num_of[d["element"]], **{k: v for k, v in d.items() if k != "check"}}
                             for d in case["defects"]]}

    for name, obj in (("mapping.json", mapping), ("request.json", request),
                      ("case.json", case_json), ("verify/report.json", report)):
        (case_dir / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2))
    (case_dir / "CASE.md").write_text(case_md(case, target_lang, num_of, len(elements), excluded))
    return report


def case_md(case, target_lang, num_of, n_sent, excluded):
    rows = "\n".join(
        f"| **{num_of[d['element']]}** | `{d['element']}` | {d['category']} · {d['subcategory']} | {d['report']} |"
        for d in case["defects"])
    return f"""# {case['id']} — {case['screen']} · {target_lang}

{len(case['defects'])} defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
{rows}

{n_sent} text elements are sent for this screen; {excluded} were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/{case['screen']}.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("case_ids", nargs="*")
    args = ap.parse_args()
    cases = yaml.safe_load((HERE / "cases.yml").read_text())["cases"]
    if args.case_ids:
        cases = [c for c in cases if c["id"] in args.case_ids]
    failed = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT, device_scale_factor=DPR)
        for case in cases:
            rep = build_case(page, case, args.out)
            failed += rep["verdict"] == "partial"
            print(f"{case['id']:<12} {rep['verdict']:<8} " +
                  " ".join(f"[{d['box']}:{d['verdict']}]" for d in rep["defects"]))
        browser.close()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
