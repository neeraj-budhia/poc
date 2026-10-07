# SP-ZH-002 — 02-search · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **10** | `search.cat.charts` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of '排行榜'. |
| **9** | `search.cat.newreleases` | LY · Truncation / clipping | '最新發行' is cut off mid-word by its container (no ellipsis). |
| **16** | `tab.search` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of '搜尋'. |

18 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/02-search.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
