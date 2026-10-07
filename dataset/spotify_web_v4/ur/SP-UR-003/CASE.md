# SP-UR-003 — 03-search-results · Urdu (ur)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **3** | `results.chip.songs` | TR · Raw resource key rendered | The raw resource key 'results.chip.songs' is shown instead of 'گانے'. |
| **19** | `results.seeall` | LY · Truncation / ellipsis | 'تمام گانے دیکھیں' is truncated with an ellipsis. |

19 text elements are sent for this screen; 4 were excluded as non-text.

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
