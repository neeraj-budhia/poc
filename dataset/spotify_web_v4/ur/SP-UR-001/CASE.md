# SP-UR-001 — 01-home · Urdu (ur)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **11** | `home.tile.episodes` | LY · Truncation / clipping | 'آپ کی اقساط' is cut off mid-word by its container (no ellipsis). |
| **14** | `home.card1.sub` | LY · RTL not mirrored | 'Arctic Monkeys، The Strokes، Tame Impala اور مزید' is left-aligned / LTR inside the right-to-left layout. |
| **15** | `home.card2.title` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of 'آپ کے ٹاپ گانے 2026'. |

17 text elements are sent for this screen; 4 were excluded as non-text.

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
