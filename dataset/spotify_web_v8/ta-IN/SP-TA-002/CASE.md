# SP-TA-002 — 02-search · Tamil (ta-IN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **13** | `search.cat.workout` | TR · Raw resource key rendered | The raw resource key 'search.cat.workout' is shown instead of 'உடற்பயிற்சி'. |
| **2** | `search.placeholder` | LY · Truncation / clipping | 'எதைக் கேட்க விரும்புகிறீர்கள்?' is cut off mid-word by its container (no ellipsis). |
| **6** | `search.cat.live` | LY · Truncation / ellipsis | 'நேரலை நிகழ்வுகள்' is truncated with an ellipsis. |

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
