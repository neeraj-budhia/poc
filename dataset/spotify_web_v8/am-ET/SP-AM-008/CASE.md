# SP-AM-008 — 08-library · Amharic (am-ET)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **5** | `library.chip.podcasts` | LY · Text runs off-screen | 'ፖድካስቶች እና ትዕይንቶች' runs off the edge of the screen. |
| **8** | `library.liked.sub` | TR · Unresolved placeholder | An unresolved placeholder ('📌 አጫዋች ዝርዝር • {count} ዘፈኖች') is shown instead of the value ('📌 አጫዋች ዝርዝር • 248 ዘፈኖች'). |

22 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/08-library.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
