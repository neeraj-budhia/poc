# SP-KO-010 — 10-settings · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('November 14, 2026에 $11.99로 요금제가 갱신됩니다.') instead of the local one ('2026년 11월 14일에 ₩10,900으로 요금제가 갱신됩니다.'). |
| **19** | `settings.logout` | TR · Raw resource key rendered | The raw resource key 'settings.logout' is shown instead of '로그아웃'. |
| **11** | `settings.explicit.sub` | LY · Overlapping text | '청소년 유해 콘텐츠를 재생하려면 켜세요. 청소년 유해 콘텐츠에는 19 태그가 표시됩니다.' overlaps the text element above it. |

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
