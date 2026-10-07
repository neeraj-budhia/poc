# SP-TA-003 — 03-search-results · Tamil (ta-IN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **8** | `results.r1.sub` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'கலைஞர்' are clipped by a too-small line box. |
| **12** | `results.r3.sub` | LY · Truncation / ellipsis | 'ஆல்பம் • Arctic Monkeys • 2013' is truncated with an ellipsis. |
| **16** | `results.r5.sub` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of 'பாடல் • Arctic Monkeys'. |

23 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/03-search-results.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
