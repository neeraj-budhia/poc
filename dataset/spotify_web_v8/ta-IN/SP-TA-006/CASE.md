# SP-TA-006 — 06-now-playing · Tamil (ta-IN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **7** | `np.devices` | LY · Overlapping text | 'கிடைக்கும் சாதனங்கள்' overlaps the text element above it. |
| **1** | `np.playingfrom` | LY · Truncation / clipping | 'பிளேலிஸ்ட்டிலிருந்து இயக்கப்படுகிறது' is cut off mid-word by its container (no ellipsis). |
| **9** | `np.lyrics.header` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of 'பாடல் வரிகள் முன்னோட்டம்'. |

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
