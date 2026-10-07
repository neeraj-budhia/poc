# SP-RU-005 — 05-premium · Russian (ru-RU)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **5** | `premium.cta.trial` | LY · Text runs off-screen | 'Попробовать бесплатно 1 месяц' runs off the edge of the screen. |
| **18** | `tab.library` | TR · Raw resource key rendered | The raw resource key 'tab.library' is shown instead of 'Моя медиатека'. |
| **14** | `premium.plan.family.feat` | TR · Unresolved placeholder | An unresolved placeholder ('До {count} аккаунтов Premium') is shown instead of the value ('До 6 аккаунтов Premium'). |

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
