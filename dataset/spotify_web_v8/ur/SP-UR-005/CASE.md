# SP-UR-005 — 05-premium · Urdu (ur)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **1** | `premium.title` | TR · Raw resource key rendered | The raw resource key 'premium.title' is shown instead of 'Premium'. |
| **11** | `premium.plan.duo.feat` | LY · Overlapping text | '2 Premium اکاؤنٹس' overlaps the text element above it. |
| **14** | `premium.plan.family.feat` | TR · Unresolved placeholder | An unresolved placeholder ('زیادہ سے زیادہ {count} Premium اکاؤنٹس') is shown instead of the value ('زیادہ سے زیادہ 6 Premium اکاؤنٹس'). |

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
