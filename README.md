# Spotify web localization testbed

Spotify-style screens rendered in headless Chromium, with localization defects planted in the
DOM/CSS of the target render. Output case packs use the same layout as the Android packs
(`~/Downloads/android/<lang>/<ID>/`).

## Coverage
9 languages, one per untested script family / sub-script (de, ja, ar, hi are excluded as already tested):
vi-VN (Latin, stacked diacritics) · ur (Arabic-script, Nastaliq, RTL) · he-IL (Hebrew, RTL) · ru-RU (Cyrillic) ·
zh-TW (CJK Traditional) · ko-KR (Hangul) · ta-IN (Indic, non-Devanagari) · th-TH (Thai) · am-ET (Ethiopic)

10 screens × 9 languages = 90 defect cases (2–3 defects each, 226 total) + 9 clean controls (`*-C01`).

## Pipeline
```
strings/<code>.json   clean target strings (+ `_fmt`: en-US-formatted variants for FORMAT defects)
screens/*.html        templates; every text element has data-k="<string key>"
gen_cases.py          → cases.yml (generated ground truth; rotates 12 defect kinds per language)
build.py              → dataset/spotify_web_v8/<code>/<ID>/ (renders, plants, verifies)
```
```
.venv/bin/python spotify_testbed/gen_cases.py
.venv/bin/python spotify_testbed/build.py --out dataset/spotify_web_v8 [CASE_ID ...]
```
`build.py` exits non-zero if any planted defect fails its render check (`verify/report.json`).

## Defect kinds
| Layer | Kind | Check |
|---|---|---|
| string | untranslated, raw_key, placeholder, mojibake, tofu, format | target renders the planted text |
| css | clip_h, ellipsis | scrollWidth > clientWidth |
| css | clip_v | content height < 0.9 × font-size |
| css | overlap | box intersects another text element > 15% |
| css | offscreen | box extends past the 360px screen edge |
| css (RTL only) | rtl_ltr | computed direction ltr / text-align left |

CSS defects are sized from the element's own measured box, so they work for any script.

## Differences from the Android packs
- `source/*.html` (rendered DOM) instead of uiautomator `*.xml`.
- `case.json` has `defects[]` (multi-defect) instead of one `case_element`; `mapping.json` has `case_elements[]`.
- `case.json` adds `is_control` and `do_not_translate_boxes` (brand / name strings identical in both locales — FP probes).

## Known limitations
- Target strings are LLM-translated with **no native-speaker review**. Prices are plausible guesses
  (Spotify doesn't sell in ET or RU). Unreviewed wording can surface as engine "false positives" —
  check controls first when a language scores oddly.
- Only text fully on screen in both locales is sent (Urdu Nastaliq pushes some rows below the fold).
