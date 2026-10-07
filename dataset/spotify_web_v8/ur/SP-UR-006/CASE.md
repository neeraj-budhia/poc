# SP-UR-006 — 06-now-playing · Urdu (ur)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **7** | `np.devices` | TR · Untranslated string | 'Devices available' is shown in English instead of 'آلات دستیاب ہیں'. |
| **8** | `np.share` | LY · Text runs off-screen | 'شیئر کریں' runs off the edge of the screen. |

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
