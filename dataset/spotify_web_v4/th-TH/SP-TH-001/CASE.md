# SP-TH-001 — 01-home · Thai (th-TH)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **6** | `home.tile.liked` | LY · Truncation / clipping | 'เพลงที่ชอบ' is cut off mid-word by its container (no ellipsis). |
| **19** | `tab.search` | GL · Missing glyphs (tofu boxes) | Characters render as empty boxes (missing font glyphs) instead of 'ค้นหา'. |
| **17** | `home.sec.recent` | LY · Vertical clipping (glyph tops/bottoms cut) | The tops/bottoms of the glyphs in 'เล่นล่าสุด' are clipped by a too-small line box. |

21 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/01-home.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
