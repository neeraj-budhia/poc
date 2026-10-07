# SP-KO-005 — 05-premium · Korean (ko-KR)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **14** | `premium.plan.family.feat` | LY · Text runs off-screen | 'Premium 계정 최대 6개' runs off the edge of the screen. |
| **4** | `premium.hero.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('이후 월 $11.99. 언제든지 해지할 수 있습니다.') instead of the local one ('이후 월 ₩10,900. 언제든지 해지할 수 있습니다.'). |

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
