# SP-RU-006 — 06-now-playing · Russian (ru-RU)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **8** | `np.share` | TR · Untranslated string | 'Share' is shown in English instead of 'Поделиться'. |
| **1** | `np.playingfrom` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of 'Воспроизводится из плейлиста'. |
| **7** | `np.devices` | LY · Truncation / ellipsis | 'Доступные устройства' is truncated with an ellipsis. |

11 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/06-now-playing.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
