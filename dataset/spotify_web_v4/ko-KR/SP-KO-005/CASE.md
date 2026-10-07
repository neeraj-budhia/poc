# SP-KO-005 — 05-premium · Korean (ko-KR)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **18** | `tab.library` | LY · Text runs off-screen | '내 라이브러리' runs off the edge of the screen. |
| **10** | `premium.plan.duo.price` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('월 $16.99') instead of the local one ('월 ₩16,350'). |

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
