# SP-KO-009 — 09-artist · Korean (ko-KR)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **11** | `artist.seemore` | TR · Untranslated string | 'See more' is shown in English instead of '더 보기'. |
| **2** | `artist.listeners` | TR · Unresolved placeholder | An unresolved placeholder ('월별 청취자 {count}명') is shown instead of the value ('월별 청취자 24,812,331명'). |

14 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/09-artist.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
