# SP-TH-005 — 05-premium · Thai (th-TH)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **11** | `premium.plan.duo.feat` | TR · Untranslated string | '2 Premium accounts' is shown in English instead of 'บัญชี Premium 2 บัญชี'. |
| **3** | `premium.hero.title` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('ทดลองใช้ Premium 1 เดือน ฟรี ฿0'). |
| **5** | `premium.cta.trial` | LY · Text runs off-screen | 'ทดลองใช้ฟรี 1 เดือน' runs off the edge of the screen. |

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
