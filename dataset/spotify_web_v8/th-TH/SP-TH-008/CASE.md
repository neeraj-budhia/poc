# SP-TH-008 — 08-library · Thai (th-TH)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **9** | `library.episodes.title` | GL · Encoding error (mojibake) | Text is garbled by an encoding error instead of 'ตอนของคุณ'. |
| **8** | `library.liked.sub` | TR · Unresolved placeholder | An unresolved placeholder ('📌 เพลย์ลิสต์ • {count} เพลง') is shown instead of the value ('📌 เพลย์ลิสต์ • 248 เพลง'). |
| **18** | `library.add.podcasts` | LY · Text runs off-screen | 'เพิ่มพอดแคสต์และรายการ' runs off the edge of the screen. |

22 text elements are sent for this screen; 0 were excluded as non-text.

## Files

| Path | What |
|---|---|
| `request.json` | the exact `localization-check` payload for this screen |
| `mapping.json` | box → element, both boxes, percentages |
| `annotated/base.jpg`, `target.jpg` | numbered boxes burned in, same number = same element |
| `source/*.png`, `source/*.html` | screenshots and rendered DOM, both locales |
| `verify/` | per-defect render check + element crops |

Rendered from `spotify_testbed/screens/08-library.html` in headless Chromium at 360×800 CSS px @3x
(1080×2400); base and target share a coordinate space.
