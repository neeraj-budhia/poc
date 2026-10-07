# SP-AM-006 — 06-now-playing · Amharic (am-ET)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **7** | `np.devices` | LY · Truncation / clipping | 'የሚገኙ መሣሪያዎች' is cut off mid-word by its container (no ellipsis). |
| **1** | `np.playingfrom` | LY · Truncation / ellipsis | 'ከአጫዋች ዝርዝር በመጫወት ላይ' is truncated with an ellipsis. |
| **9** | `np.lyrics.header` | TR · Untranslated string | 'Lyrics preview' is shown in English instead of 'የግጥም ቅድመ-እይታ'. |

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
