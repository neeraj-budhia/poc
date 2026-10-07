# SP-TH-004 — 04-playlist · Thai (th-TH)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **3** | `playlist.madefor` | LY · Truncation / clipping | 'สร้างมาเพื่อ Neeraj' is cut off mid-word by its container (no ellipsis). |
| **5** | `playlist.btn.save` | LY · Truncation / ellipsis | 'บันทึก' is truncated with an ellipsis. |
| **13** | `playlist.updated` | TR · Raw resource key rendered | The raw resource key 'playlist.updated' is shown instead of 'อัปเดตเมื่อ 6 วันที่แล้ว'. |

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
