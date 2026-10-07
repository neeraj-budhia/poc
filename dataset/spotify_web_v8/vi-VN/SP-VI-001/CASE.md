# SP-VI-001 — 01-home · Vietnamese (vi-VN)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **14** | `home.card1.sub` | LY · Overlapping text | 'Arctic Monkeys, The Strokes, Tame Impala và nhiều nghệ sĩ khác' overlaps the text element above it. |
| **6** | `home.tile.liked` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of 'Bài hát đã thích'. |

21 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/01-home.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
