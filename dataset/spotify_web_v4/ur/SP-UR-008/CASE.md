# SP-UR-008 — 08-library · Urdu (ur)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **10** | `library.episodes.sub` | LY · Truncation / clipping | 'محفوظ اور ڈاؤن لوڈ کردہ اقساط' is cut off mid-word by its container (no ellipsis). |
| **17** | `library.add.artists` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'فنکار شامل کریں' are clipped by a too-small line box. |
| **8** | `library.liked.sub` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('📌 پلے لسٹ • 248 گانے'). |

18 text elements are sent for this screen; 4 were excluded as non-text.

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
