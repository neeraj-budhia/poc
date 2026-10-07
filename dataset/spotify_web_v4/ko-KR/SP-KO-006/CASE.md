# SP-KO-006 — 06-now-playing · Korean (ko-KR)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **1** | `np.playingfrom` | LY · Truncation / clipping | '플레이리스트에서 재생 중' is cut off mid-word by its container (no ellipsis). |
| **8** | `np.share` | LY · Truncation / ellipsis | '공유하기' is truncated with an ellipsis. |
| **4** | `np.artist` | TR · Raw resource key rendered | The raw resource key 'np.artist' is shown instead of 'Arctic Monkeys'. |

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
