# SP-KO-010 — 10-settings · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('November 14, 2026에 $11.99로 요금제가 갱신됩니다.') instead of the local one ('2026년 11월 14일에 ₩10,900으로 요금제가 갱신됩니다.'). |
| **17** | `settings.language` | LY · Truncation / ellipsis | '앱 언어' is truncated with an ellipsis. |
| **13** | `settings.datasaver` | LY · Truncation / clipping | '데이터 절약 모드' is cut off mid-word by its container (no ellipsis). |

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
