# SP-KO-002 — 02-search · Korean (ko-KR)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **17** | `tab.library` | TR · Raw resource key rendered | The raw resource key 'tab.library' is shown instead of '내 라이브러리'. |
| **13** | `search.cat.workout` | LY · Truncation / clipping | '운동' is cut off mid-word by its container (no ellipsis). |

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
