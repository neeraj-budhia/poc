# SP-ZH-003 — 03-search-results · Chinese (zh-TW)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **6** | `results.chip.albums` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of '專輯'. |
| **14** | `results.r4.sub` | LY · Overlapping text | '播放清單 • Spotify' overlaps the text element above it. |

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
