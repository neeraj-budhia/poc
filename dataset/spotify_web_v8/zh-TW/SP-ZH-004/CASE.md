# SP-ZH-004 — 04-playlist · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **2** | `playlist.desc` | TR · Raw resource key rendered | The raw resource key 'playlist.desc' is shown instead of '每週為你精選的新鮮音樂合輯。盡情享受為你挑選的新音樂和冷門好歌。每週一更新。'. |
| **13** | `playlist.updated` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '6 天前更新' are clipped by a too-small line box. |
| **5** | `playlist.btn.save` | LY · Truncation / clipping | '儲存' is cut off mid-word by its container (no ellipsis). |

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
