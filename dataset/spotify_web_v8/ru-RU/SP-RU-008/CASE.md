# SP-RU-008 — 08-library · Russian (ru-RU)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **8** | `library.liked.sub` | LY · Overlapping text | '📌 Плейлист • 248 треков' overlaps the text element above it. |
| **16** | `library.album1.sub` | TR · Untranslated string | 'Album • Tame Impala' is shown in English instead of 'Альбом • Tame Impala'. |
| **1** | `library.title` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'Моя медиатека' are clipped by a too-small line box. |

22 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/08-library.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
