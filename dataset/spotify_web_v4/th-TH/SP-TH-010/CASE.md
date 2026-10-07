# SP-TH-010 — 10-settings · Thai (th-TH)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **8** | `settings.crossfade.val` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('5 วินาที'). |
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('แพ็กเกจของคุณจะต่ออายุในวันที่ November 14, 2026 ในราคา $11.99') instead of the local one ('แพ็กเกจของคุณจะต่ออายุในวันที่ 14 พฤศจิกายน 2569 ในราคา ฿139'). |
| **17** | `settings.language` | LY · Truncation / ellipsis | 'ภาษาของแอป' is truncated with an ellipsis. |

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
