# SP-ZH-008 — 08-library · Chinese (zh-TW)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **5** | `library.chip.podcasts` | LY · Text runs off-screen | 'Podcast 和節目' runs off the edge of the screen. |
| **1** | `library.title` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in '你的音樂庫' are clipped by a too-small line box. |
| **8** | `library.liked.sub` | TR · Unresolved placeholder | An unresolved placeholder ('📌 播放清單 • {count} 首歌曲') is shown instead of the value ('📌 播放清單 • 248 首歌曲'). |

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
