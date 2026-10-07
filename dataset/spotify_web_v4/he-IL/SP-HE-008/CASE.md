# SP-HE-008 — 08-library · Hebrew (he-IL)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **14** | `library.artist1.sub` | TR · Untranslated string | 'Artist' is shown in English instead of 'אמן'. |
| **17** | `library.add.artists` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'הוספת אמנים' are clipped by a too-small line box. |

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
