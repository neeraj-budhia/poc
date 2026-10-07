# SP-UR-002 — 02-search · Urdu (ur)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **9** | `search.cat.newreleases` | LY · Truncation / clipping | 'نئی ریلیزز' is cut off mid-word by its container (no ellipsis). |
| **7** | `search.cat.madeforyou` | LY · Truncation / ellipsis | 'آپ کے لیے تیار کردہ' is truncated with an ellipsis. |
| **12** | `search.cat.hiphop` | TR · Untranslated string | 'Hip-Hop' is shown in English instead of 'ہپ ہاپ'. |

14 text elements are sent for this screen; 4 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/02-search.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
