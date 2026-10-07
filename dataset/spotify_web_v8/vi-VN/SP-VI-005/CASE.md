# SP-VI-005 — 05-premium · Vietnamese (vi-VN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **5** | `premium.cta.trial` | LY · Text runs off-screen | 'Dùng thử miễn phí 1 tháng' runs off the edge of the screen. |
| **8** | `premium.plan.individual.feat` | LY · Truncation / clipping | '1 tài khoản Premium' is cut off mid-word by its container (no ellipsis). |
| **13** | `premium.plan.family.price` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('$19.99 / tháng') instead of the local one ('95.000 ₫ / tháng'). |

19 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/05-premium.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
