# SP-UR-006 — 06-now-playing · Urdu (ur)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **8** | `np.share` | TR · Untranslated string | 'Share' is shown in English instead of 'شیئر کریں'. |
| **7** | `np.devices` | LY · Text runs off-screen | 'آلات دستیاب ہیں' runs off the edge of the screen. |

10 text elements are sent for this screen; 1 were excluded as non-text.

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
