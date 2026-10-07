# SP-AM-005 — 05-premium · Amharic (am-ET)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **15** | `premium.legal` | LY · Overlapping text | 'ውሎች ተፈጻሚ ይሆናሉ። ቅናሹ 31 ኦክቶበር 2026 ላይ ያበቃል። ለግለሰብ ዕቅድ ብቻ።' overlaps the text element above it. |
| **13** | `premium.plan.family.price` | TR · Raw resource key rendered | The raw resource key 'premium.plan.family.price' is shown instead of 'US$ 8.99 / ወር'. |

19 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/05-premium.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
