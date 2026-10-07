# SP-ZH-001 — 01-home · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **19** | `tab.search` | TR · Untranslated string | 'Search' is shown in English instead of '搜尋'. |
| **3** | `home.chip.music` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of '音樂'. |
| **10** | `home.tile.chill` | LY · Truncation / ellipsis | '放鬆氛圍' is truncated with an ellipsis. |

21 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/01-home.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
