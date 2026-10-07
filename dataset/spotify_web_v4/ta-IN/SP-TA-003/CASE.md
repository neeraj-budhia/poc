# SP-TA-003 — 03-search-results · Tamil (ta-IN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `results.chip.artists` | TR · Raw resource key rendered | The raw resource key 'results.chip.artists' is shown instead of 'கலைஞர்கள்'. |
| **5** | `results.chip.playlists` | LY · Truncation / clipping | 'பிளேலிஸ்ட்கள்' is cut off mid-word by its container (no ellipsis). |
| **19** | `results.seeall` | LY · Truncation / ellipsis | 'எல்லாப் பாடல்களையும் காட்டு' is truncated with an ellipsis. |

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
