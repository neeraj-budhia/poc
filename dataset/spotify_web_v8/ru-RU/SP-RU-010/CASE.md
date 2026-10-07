# SP-RU-010 — 10-settings · Russian (ru-RU)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **16** | `settings.storage.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('Использовано: 1.2 GB • Свободно: 48.6 GB') instead of the local one ('Использовано: 1,2 ГБ • Свободно: 48,6 ГБ'). |
| **14** | `settings.datasaver.sub` | LY · Overlapping text | 'Устанавливает низкое качество музыки и отключает Canvas.' overlaps the text element above it. |

20 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/10-settings.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
