# SP-UR-009 — 09-artist · Urdu (ur)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **2** | `artist.listeners` | LY · RTL not mirrored | '24,812,331 ماہانہ سامعین' is left-aligned / LTR inside the right-to-left layout. |
| **14** | `artist.latest.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('October 17, 2025 • البم') instead of the local one ('17 اکتوبر 2025 • البم'). |

14 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/09-artist.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
