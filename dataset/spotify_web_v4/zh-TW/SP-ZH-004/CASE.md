# SP-ZH-004 — 04-playlist · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `playlist.meta` | LY · Text runs off-screen | '30 首歌曲，約 2 小時 5 分鐘' runs off the edge of the screen. |
| **13** | `playlist.updated` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '6 天前更新' are clipped by a too-small line box. |
| **6** | `playlist.btn.download` | TR · Untranslated string | 'Download' is shown in English instead of '下載'. |

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
