# SP-RU-001 — 01-home · Russian (ru-RU)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **15** | `home.card2.title` | TR · Untranslated string | 'Your Top Songs 2026' is shown in English instead of 'Мои лучшие треки 2026'. |
| **6** | `home.tile.liked` | LY · Truncation / clipping | 'Любимые треки' is cut off mid-word by its container (no ellipsis). |

21 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/01-home.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
