# SP-TA-009 — 09-artist · Tamil (ta-IN)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **2** | `artist.listeners` | TR · Unresolved placeholder | An unresolved placeholder ('{count} மாதாந்திரக் கேட்போர்') is shown instead of the value ('2,48,12,331 மாதாந்திரக் கேட்போர்'). |
| **9** | `artist.p3.title` | TR · Raw resource key rendered | The raw resource key 'artist.p3.title' is shown instead of 'Borderline'. |

14 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/09-artist.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
