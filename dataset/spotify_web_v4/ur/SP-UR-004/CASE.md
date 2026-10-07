# SP-UR-004 — 04-playlist · Urdu (ur)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **6** | `playlist.btn.download` | TR · Untranslated string | 'Download' is shown in English instead of 'ڈاؤن لوڈ کریں'. |
| **4** | `playlist.meta` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '30 گانے، تقریباً 2 گھنٹے 5 منٹ' are clipped by a too-small line box. |
| **13** | `playlist.updated` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of '6 دن پہلے اپ ڈیٹ ہوئی'. |

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
