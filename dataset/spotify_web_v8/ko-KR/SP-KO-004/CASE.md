# SP-KO-004 — 04-playlist · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **13** | `playlist.updated` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '6일 전 업데이트됨' are clipped by a too-small line box. |
| **3** | `playlist.madefor` | LY · Truncation / ellipsis | 'Neeraj님을 위해 제작됨' is truncated with an ellipsis. |
| **2** | `playlist.desc` | TR · Untranslated string | 'Your weekly mixtape of fresh music. Enjoy new music and deep cuts picked for you. Updates every Monday.' is shown in English instead of '매주 새로운 음악으로 채워지는 나만의 믹스테이프. 회원님을 위해 엄선한 신곡과 숨은 명곡을 즐겨 보세요. 매주 월요일에 업데이트됩니다.'. |

13 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/04-playlist.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
