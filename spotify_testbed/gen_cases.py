#!/usr/bin/env python3
"""Generate cases.yml: per language, 10 defect cases (one per screen, 2–3 planted defects each)
plus 1 clean control case.

Defect kinds rotate per language so every language gets the full mix; RTL-only and
script-sensitive kinds are weighted per locale. Text for string-layer defects is resolved
here (from strings/*.json) so cases.yml is the complete, reviewable ground truth.
Deterministic: same strings in → same cases.yml out.
"""
import json
import random
import re
import unicodedata
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

import build

HERE = Path(__file__).parent
LANGS = ["vi-VN", "ur", "he-IL", "ru-RU", "zh-TW", "ko-KR", "ta-IN", "th-TH", "am-ET"]
TAG = {"vi-VN": "VI", "ur": "UR", "he-IL": "HE", "ru-RU": "RU", "zh-TW": "ZH",
       "ko-KR": "KO", "ta-IN": "TA", "th-TH": "TH", "am-ET": "AM"}
RTL = {"ur", "he-IL"}
TALL_MARKS = {"vi-VN", "ur", "ta-IN", "th-TH"}  # stacked diacritics / tone marks / Nastaliq height

# Element roles per screen: which elements each CSS-layer defect can sensibly hit.
#   label: single-line UI labels (buttons, chips, tile names, row titles) → clip / ellipsis / offscreen
#   title: large headings → vertical clipping
#   body:  block text with a text neighbour above → overlap, RTL-not-mirrored
ROLES = {
    "01-home": {"label": ["home.chip.podcasts", "home.tile.liked", "home.tile.episodes", "home.tile.chill", "home.card2.title"],
                "title": ["home.greeting", "home.sec.madeforyou", "home.sec.recent"],
                "body": ["home.card1.sub", "home.card2.sub"]},
    "02-search": {"label": ["search.cat.live", "search.cat.madeforyou", "search.cat.newreleases", "search.placeholder", "search.cat.workout"],
                  "title": ["search.title", "search.sec.start", "search.sec.browse"],
                  "body": ["search.sec.browse"]},
    "03-search-results": {"label": ["results.chip.playlists", "results.chip.artists", "results.seeall", "results.r3.sub"],
                          "title": ["results.r1.sub", "results.chip.songs"],
                          "body": ["results.r2.sub", "results.r4.sub"]},
    "04-playlist": {"label": ["playlist.btn.download", "playlist.btn.save", "playlist.madefor", "playlist.meta"],
                    "title": ["playlist.updated", "playlist.meta"],
                    "body": ["playlist.desc", "playlist.meta", "playlist.updated"]},
    "05-premium": {"label": ["premium.cta.trial", "premium.plan.individual.feat", "premium.plan.family.feat", "tab.library"],
                   "title": ["premium.hero.title", "premium.plan.individual.name", "premium.plan.family.name"],
                   "body": ["premium.hero.sub", "premium.plan.duo.feat", "premium.legal"]},
    "06-now-playing": {"label": ["np.devices", "np.share", "np.playingfrom"],
                       "title": ["np.lyrics.header", "np.playingfrom"],
                       "body": ["np.lyrics.header", "np.devices"]},
    "07-lyrics": {"label": ["lyrics.translate", "lyrics.report", "lyrics.share"],
                  "title": ["lyrics.translate", "lyrics.report"],
                  "body": ["lyrics.credit", "lyrics.translate"]},
    "08-library": {"label": ["library.chip.podcasts", "library.add.podcasts", "library.episodes.sub", "library.chip.playlists"],
                   "title": ["library.title", "library.liked.title", "library.add.artists"],
                   "body": ["library.episodes.sub", "library.liked.sub", "library.artist1.sub"]},
    "09-artist": {"label": ["artist.follow", "artist.seemore", "artist.listeners"],
                  "title": ["artist.sec.popular", "artist.sec.release"],
                  "body": ["artist.listeners", "artist.latest.sub"]},
    "10-settings": {"label": ["settings.logout", "settings.gapless", "settings.datasaver", "settings.language"],
                    "title": ["settings.sec.playback", "settings.sec.data", "settings.title"],
                    "body": ["settings.crossfade.sub", "settings.explicit.sub", "settings.datasaver.sub", "settings.plan.sub"]},
}
SCREENS = list(ROLES)

# kind → (layer, category, subcategory, check, role or None for string kinds)
KINDS = {
    "untranslated": ("text", "TR", "Untranslated string", "text", None),
    "raw_key": ("text", "TR", "Raw resource key rendered", "text", None),
    "placeholder": ("text", "TR", "Unresolved placeholder", "text", None),
    "mojibake": ("text", "GL", "Encoding error (mojibake)", "text", None),
    "tofu": ("text", "GL", "Missing glyphs (tofu boxes)", "text", None),
    "format": ("text", "FMT", "Number / date / currency not localized", "text", None),
    "clip_h": ("css", "LY", "Truncation / clipping", "clipped", "label"),
    "ellipsis": ("css", "LY", "Truncation / ellipsis", "clipped", "label"),
    "clip_v": ("css", "LY", "Vertical clipping (glyph tops/bottoms cut)", "clipped_v", "title"),
    "overlap": ("css", "LY", "Overlapping text", "overlap", "body"),
    "offscreen": ("css", "LY", "Text runs off-screen", "offscreen", "label"),
    "rtl_ltr": ("css", "LY", "RTL not mirrored", "direction", "body"),
}
STRING_KINDS = [k for k, v in KINDS.items() if v[0] == "text"]
CSS_KINDS = [k for k, v in KINDS.items() if v[0] == "css"]
# strings whose number is a runtime variable ({count} etc.) — not titles/names that merely contain digits
COUNT_KEYS = {"premium.hero.title", "premium.plan.individual.feat", "premium.plan.duo.feat", "premium.plan.family.feat",
              "premium.cta.trial", "playlist.meta", "playlist.updated", "library.liked.sub", "artist.listeners",
              "settings.crossfade.val"}
DIGITS = re.compile(r"\d+")
# a whole number incl. its group separators ("24,812,331", "24 812 331") — a runtime placeholder
# bug replaces the entire value, not its first digit group
NUMBER = re.compile(r"\d(?:[\d.,\u00a0\u202f ]*\d)?")
MIN_ELLIPSIS_CHARS = 6  # shorter labels leave no room for "…" once cut to 55%
TIME = re.compile(r"^-?\d+:\d\d$")


def clean_target(page, lang, screen):
    """(clean target elements by key, keys fully on screen in BOTH clean base and clean target)."""
    base = {e["key"] for e in build.render(page, screen, "en-US", [])[0] if e["visible"] and e["text"]}
    tgt = {e["key"]: e for e in build.render(page, screen, lang, [])[0]}
    return tgt, {k for k, e in tgt.items() if e["visible"] and e["text"] and k in base}


def clear_path(key, els, lang):
    """True if nothing on the same row sits between the element and the edge it reads towards,
    so pushing it off-screen cannot land it on a neighbour."""
    x0, y0, x1, y1 = els[key]["box"]
    for k, e in els.items():
        if k == key or not e["visible"] or not (e["text"] or e.get("obstacle")):
            continue
        a0, b0, a1, b1 = e["box"]
        if min(y1, b1) - max(y0, b0) <= 0.3 * min(y1 - y0, b1 - b0):
            continue  # different row
        if (lang in RTL and a1 <= x0 + 1) or (lang not in RTL and a0 >= x1 - 1):
            return False
    return True


def kind_queue(lang, rng):
    q = ["untranslated", "raw_key", "placeholder", "mojibake", "tofu", "format",
         "clip_h", "ellipsis", "clip_v", "overlap", "offscreen"] * 2
    q += ["untranslated", "clip_h"]  # the two most common real-world defects
    if lang in RTL:
        q += ["rtl_ltr"] * 3
    if lang in TALL_MARKS:
        q += ["clip_v"]
    rng.shuffle(q)
    return q


def defect_text(kind, key, en, tgt, fmt):
    t = tgt[key]
    if kind == "untranslated":
        return en[key] if en[key] != t else None
    if kind == "raw_key":
        return None if TIME.match(t) else key  # a timestamp is computed, never a string resource
    if kind == "placeholder":
        if key not in COUNT_KEYS or TIME.match(t) or not DIGITS.search(t):
            return None
        m = NUMBER.search(t)
        # a number next to a currency sign is a price slot: the runtime variable is an amount
        near = t[max(m.start() - 2, 0):m.start()] + t[m.end():m.end() + 2]
        name = "{amount}" if any(c in near for c in "$€£¥₩₹₪₽฿₫") else "{count}"
        return t[:m.start()] + name + t[m.end():]
    if kind == "mojibake":
        if t.isascii():
            return None
        return t.encode("utf-8").decode("cp1252", errors="replace")
    if kind == "tofu":
        if t.isascii():
            return None
        # a missing font draws one box per code point it lacks. Every font has Latin-1, so only
        # code points above U+00FF are boxed (Vietnamese ổ ư đ, not à á); NFC keeps precomposed
        # letters whole, and Thai/Indic vowel signs (separate code points) get their own box
        return "".join("□" if ord(c) > 0xFF and (c.isalpha() or unicodedata.category(c).startswith("M")) else c
                       for c in unicodedata.normalize("NFC", t))
    if kind == "format":
        return fmt.get(key)
    raise ValueError(kind)


def report_line(kind, key, en, tgt, text):
    # invisible layout characters (word joiners) never belong in human-readable report text
    e, t = en[key], tgt[key].replace("\u2060", "")
    return {
        "untranslated": f"'{e}' is shown in English instead of '{t}'.",
        "raw_key": f"The raw resource key '{key}' is shown instead of '{t}'.",
        "placeholder": f"An unresolved placeholder ('{text}') is shown instead of the value ('{t}').",
        "mojibake": f"Text is garbled by an encoding error instead of '{t}'.",
        "tofu": f"Characters render as empty boxes (missing font glyphs) instead of '{t}'.",
        "format": f"Number/date/currency uses the US format ('{text}') instead of the local one ('{t}').",
        "clip_h": f"'{t}' is cut off mid-word by its container (no ellipsis).",
        "ellipsis": f"'{t}' is truncated with an ellipsis.",
        "clip_v": f"The tops/bottoms of the glyphs in '{t}' are clipped by a too-small line box.",
        "overlap": f"'{t}' overlaps the text element above it.",
        "offscreen": f"'{t}' runs off the edge of the screen.",
        "rtl_ltr": f"'{t}' is left-aligned / LTR inside the right-to-left layout.",
    }[kind]


def pick(kind, screen, visible, els, lang, used, en, tgt, fmt, rng):
    layer, cat, sub, check, role = KINDS[kind]
    pool = ROLES[screen][role] if role else sorted(visible)
    pool = [k for k in pool if k not in used and k in visible]
    if kind == "ellipsis":
        pool = [k for k in pool if len(tgt[k].strip()) >= MIN_ELLIPSIS_CHARS]
    if kind == "offscreen":
        pool = [k for k in pool if clear_path(k, els, lang)]
    rng.shuffle(pool)
    for key in pool:
        d = {"element": key, "kind": kind, "category": cat, "subcategory": sub, "check": check}
        if layer == "text":
            text = defect_text(kind, key, en, tgt, fmt)
            if not text or text == tgt[key]:
                continue
            d["text"] = text
        else:
            d["op"] = kind
        d["report"] = report_line(kind, key, en, tgt, d.get("text"))
        return d
    return None


def cases_for(page, lang, li, en):
    tgt = json.loads((HERE / "strings" / f"{lang}.json").read_text())
    fmt = tgt.pop("_fmt", {})
    rng = random.Random(f"spotify-{lang}")
    queue = kind_queue(lang, rng)
    out = []
    for si, screen in enumerate(SCREENS):
        els, visible = clean_target(page, lang, screen)
        n = 3 if (si + li) % 3 else 2
        defects, used = [], set()
        # at least one string-layer and one css-layer defect per case
        need = {"text", "css"}
        tries = 0
        while len(defects) < n and tries < 200:
            tries += 1
            if not queue:
                queue.extend(kind_queue(lang, rng))
            kind = queue.pop(0)
            layer = KINDS[kind][0]
            if (kind == "rtl_ltr" and lang not in RTL) or \
               (need and layer not in need and len(defects) >= n - len(need)) or \
               any(d["kind"] == kind for d in defects):
                queue.append(kind)
                continue
            d = pick(kind, screen, visible, els, lang, used, en, tgt, fmt, rng)
            if d is None:
                queue.append(kind)
                continue
            # trial render: reject a defect that damages anything it doesn't account for
            trial = {e["key"]: e for e in build.render(page, screen, lang, defects + [d])[0]}
            if build.collateral(els, trial, defects + [d]):
                used.add(d["element"])
                queue.append(kind)
                continue
            defects.append(d)
            used.add(d["element"])
            need.discard(layer)
        out.append({"id": f"SP-{TAG[lang]}-{si + 1:03d}", "lang": lang, "screen": screen, "defects": defects})
    out.append({"id": f"SP-{TAG[lang]}-C01", "lang": lang, "screen": SCREENS[li % len(SCREENS)], "defects": []})
    return out


def main():
    en = json.loads((HERE / "strings" / "en-US.json").read_text())
    cases = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=build.VIEWPORT)
        for li, lang in enumerate(LANGS):
            cases += cases_for(page, lang, li, en)
        browser.close()
    header = ("# GENERATED by gen_cases.py — edit the generator, not this file.\n"
              "# One case = one screen variant with 2–3 planted defects; *-C01 = clean control.\n")
    (HERE / "cases.yml").write_text(header + yaml.safe_dump({"cases": cases}, allow_unicode=True, sort_keys=False, width=200))
    kinds = {}
    for c in cases:
        for d in c["defects"]:
            kinds[d["kind"]] = kinds.get(d["kind"], 0) + 1
    print(f"{len(cases)} cases, {sum(kinds.values())} defects:", dict(sorted(kinds.items())))


if __name__ == "__main__":
    main()
