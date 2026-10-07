# SP-AM-003 — 03-search-results · Amharic (am-ET)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **18** | `results.r6.sub` | TR · Untranslated string | 'Playlist • Spotify' is shown in English instead of 'አጫዋች ዝርዝር • Spotify'. |
| **12** | `results.r3.sub` | TR · Raw resource key rendered | The raw resource key 'results.r3.sub' is shown instead of 'አልበም • Arctic Monkeys • 2013'. |
| **19** | `results.seeall` | LY · Truncation / clipping | 'ሁሉንም ዘፈኖች ይመልከቱ' is cut off mid-word by its container (no ellipsis). |

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
