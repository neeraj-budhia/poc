# SP-UR-010 — 10-settings · Urdu (ur)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **16** | `settings.storage.sub` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('1.2 GB استعمال شدہ • 48.6 GB خالی'). |
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('آپ کا پلان November 14, 2026 کو $11.99 میں تجدید ہو جائے گا۔') instead of the local one ('آپ کا پلان 14 نومبر 2026 کو Rs 349 میں تجدید ہو جائے گا۔'). |
| **1** | `settings.title` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'ترتیبات' are clipped by a too-small line box. |

20 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/10-settings.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
