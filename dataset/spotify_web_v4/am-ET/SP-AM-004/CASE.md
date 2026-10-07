# SP-AM-004 — 04-playlist · Amharic (am-ET)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **3** | `playlist.madefor` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of 'ለNeeraj የተሰራ'. |
| **4** | `playlist.meta` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '30 ዘፈኖች፣ በግምት 2 ሰዓት 5 ደቂቃ' are clipped by a too-small line box. |
| **5** | `playlist.btn.save` | LY · Text runs off-screen | 'አስቀምጥ' runs off the edge of the screen. |

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
