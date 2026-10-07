# SP-VI-005 — 05-premium · Vietnamese (vi-VN)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **3** | `premium.hero.title` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('Dùng thử 1 tháng gói Premium với giá 0 ₫'). |
| **18** | `tab.library` | TR · Untranslated string | 'Your Library' is shown in English instead of 'Thư viện'. |
| **12** | `premium.plan.family.name` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'Gia đình' are clipped by a too-small line box. |

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
