# SP-TA-005 — 05-premium · Tamil (ta-IN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **5** | `premium.cta.trial` | LY · Text runs off-screen | '1 மாதம் இலவசமாக முயற்சிக்கவும்' runs off the edge of the screen. |
| **18** | `tab.library` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of 'உங்கள் லைப்ரரி'. |
| **11** | `premium.plan.duo.feat` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('2 Premium கணக்குகள்'). |

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
