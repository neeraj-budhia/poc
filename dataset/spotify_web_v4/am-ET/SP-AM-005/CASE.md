# SP-AM-005 — 05-premium · Amharic (am-ET)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **3** | `premium.hero.title` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('Premium ለ1 ወር በUS$ 0 ይሞክሩ'). |
| **11** | `premium.plan.duo.feat` | LY · Overlapping text | '2 የPremium መለያዎች' overlaps the text element above it. |

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
