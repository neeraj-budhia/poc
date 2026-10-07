# SP-ZH-005 — 05-premium · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `premium.hero.sub` | LY · Overlapping text | '之後每月只要 NT$149。可隨時取消。' overlaps the text element above it. |
| **8** | `premium.plan.individual.feat` | LY · Truncation / ellipsis | '1 個 Premium 帳戶' is truncated with an ellipsis. |
| **13** | `premium.plan.family.price` | TR · Raw resource key rendered | The raw resource key 'premium.plan.family.price' is shown instead of 'NT$268 / 月'. |

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
