# SP-ZH-005 — 05-premium · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **14** | `premium.plan.family.feat` | TR · Raw resource key rendered | The raw resource key 'premium.plan.family.feat' is shown instead of '最多 6 個 Premium 帳戶'. |
| **3** | `premium.hero.title` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '以 NT$0 試用 Premium 1 個月' are clipped by a too-small line box. |
| **15** | `premium.legal` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('適用相關條款。優惠於 October 31, 2026 結束。僅限個人方案。') instead of the local one ('適用相關條款。優惠於 2026年10月31日結束。僅限個人方案。'). |

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
