# SP-HE-001 — 01-home · Hebrew (he-IL)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **11** | `home.tile.episodes` | TR · Untranslated string | 'Your Episodes' is shown in English instead of 'הפרקים שלך'. |
| **16** | `home.card2.sub` | LY · RTL not mirrored | 'השירים שהכי אהבת השנה, כולם במקום אחד.' is left-aligned / LTR inside the right-to-left layout. |
| **15** | `home.card2.title` | LY · Text runs off-screen | 'השירים המובילים שלך 2026' runs off the edge of the screen. |

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
