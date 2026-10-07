# SP-KO-007 — 07-lyrics · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **9** | `lyrics.translate` | TR · Untranslated string | 'Show translation' is shown in English instead of '번역 보기'. |
| **10** | `lyrics.credit` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of 'Musixmatch에서 가사 제공'. |
| **11** | `lyrics.share` | LY · Truncation / ellipsis | '공유하기' is truncated with an ellipsis. |

12 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/07-lyrics.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
