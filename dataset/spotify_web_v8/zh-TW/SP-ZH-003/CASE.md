# SP-ZH-003 — 03-search-results · Chinese (zh-TW)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **10** | `results.r2.sub` | LY · Overlapping text | '歌曲 • Arctic Monkeys' overlaps the text element above it. |
| **16** | `results.r5.sub` | TR · Untranslated string | 'Song • Arctic Monkeys' is shown in English instead of '歌曲 • Arctic Monkeys'. |

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
