# SP-TA-008 — 08-library · Tamil (ta-IN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **8** | `library.liked.sub` | LY · Overlapping text | '📌 பிளேலிஸ்ட் • 248 பாடல்கள்' overlaps the text element above it. |
| **5** | `library.chip.podcasts` | LY · Text runs off-screen | 'பாட்காஸ்ட்கள் & நிகழ்ச்சிகள்' runs off the edge of the screen. |
| **9** | `library.episodes.title` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of 'உங்கள் எபிசோடுகள்'. |

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
