# SP-TA-010 — 10-settings · Tamil (ta-IN)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('உங்கள் திட்டம் November 14, 2026 அன்று $11.99-க்குப் புதுப்பிக்கப்படும்.') instead of the local one ('உங்கள் திட்டம் 14 நவம்பர், 2026 அன்று ₹139-க்குப் புதுப்பிக்கப்படும்.'). |
| **14** | `settings.datasaver.sub` | LY · Overlapping text | 'உங்கள் இசைத் தரத்தைக் குறைவாக அமைத்து, கேன்வாஸை முடக்கும்.' overlaps the text element above it. |

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
