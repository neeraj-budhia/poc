# SP-TA-004 — 04-playlist · Tamil (ta-IN)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `playlist.meta` | LY · Text runs off-screen | '30 பாடல்கள், சுமார் 2 மணி 5 நிமி' runs off the edge of the screen. |
| **5** | `playlist.btn.save` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of 'சேமி'. |

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
