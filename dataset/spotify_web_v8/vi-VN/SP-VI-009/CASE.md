# SP-VI-009 — 09-artist · Vietnamese (vi-VN)

2 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `artist.sec.popular` | TR · Untranslated string | 'Popular' is shown in English instead of 'Phổ biến'. |
| **2** | `artist.listeners` | TR · Unresolved placeholder | An unresolved placeholder ('{count} người nghe hằng tháng') is shown instead of the value ('24.812.331 người nghe hằng tháng'). |

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
