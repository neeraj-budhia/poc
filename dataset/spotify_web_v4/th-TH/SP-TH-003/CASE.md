# SP-TH-003 — 03-search-results · Thai (th-TH)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **12** | `results.r3.sub` | LY · Truncation / ellipsis | 'อัลบั้ม • Arctic Monkeys • 2556' is truncated with an ellipsis. |
| **3** | `results.chip.songs` | TR · Untranslated string | 'Songs' is shown in English instead of 'เพลง'. |

23 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/03-search-results.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
