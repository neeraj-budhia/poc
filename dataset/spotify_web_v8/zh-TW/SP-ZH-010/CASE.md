# SP-ZH-010 — 10-settings · Chinese (zh-TW)

1 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('你的方案將於 November 14, 2026 續訂，費用為 $11.99。') instead of the local one ('你的方案將於 2026年11月14日續訂，費用為 NT$149。'). |

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
