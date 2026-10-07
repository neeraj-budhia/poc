# SP-KO-001 — 01-home · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **14** | `home.card1.sub` | LY · Overlapping text | 'Arctic Monkeys, The Strokes, Tame Impala 외' overlaps the text element above it. |
| **1** | `home.greeting` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '좋은 저녁이에요' are clipped by a too-small line box. |
| **16** | `home.card2.sub` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of '올해 가장 사랑한 곡들을 한데 모았어요.'. |

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
