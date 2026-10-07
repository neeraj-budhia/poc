# SP-RU-009 — 09-artist · Russian (ru-RU)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **2** | `artist.listeners` | TR · Unresolved placeholder | An unresolved placeholder ('{count} слушатель за месяц') is shown instead of the value ('24 812 331 слушатель за месяц'). |
| **10** | `artist.p3.plays` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('301,227,560') instead of the local one ('301 227 560'). |

14 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/09-artist.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
