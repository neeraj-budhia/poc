# SP-HE-004 — 04-playlist · Hebrew (he-IL)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **13** | `playlist.updated` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('עודכן לפני 6 ימים'). |
| **4** | `playlist.meta` | LY · Truncation / clipping | '30 שירים, בערך 2 שעות ו-5 דקות' is cut off mid-word by its container (no ellipsis). |
| **3** | `playlist.madefor` | LY · Text runs off-screen | 'נוצר עבור Neeraj' runs off the edge of the screen. |

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
