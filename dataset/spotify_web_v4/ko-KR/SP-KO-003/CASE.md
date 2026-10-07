# SP-KO-003 — 03-search-results · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **5** | `results.chip.playlists` | LY · Truncation / clipping | '플레이리스트' is cut off mid-word by its container (no ellipsis). |
| **10** | `results.r2.sub` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of '곡 • Arctic Monkeys'. |
| **16** | `results.r5.sub` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of '곡 • Arctic Monkeys'. |

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
