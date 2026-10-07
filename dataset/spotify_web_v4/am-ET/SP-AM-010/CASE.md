# SP-AM-010 — 10-settings · Amharic (am-ET)

3 defects planted on one screen (DOM/CSS edits in the target render only).

| Box | Element id | Category | What App LCA must report |
|---|---|---|---|
| **4** | `settings.plan.sub` | FMT · Number / date / currency not localized | Number/date/currency uses the US format ('ዕቅድዎ November 14, 2026 ላይ በ$5.49 ይታደሳል።') instead of the local one ('ዕቅድዎ 14 ኖቬምበር 2026 ላይ በUS$ 5.49 ይታደሳል።'). |
| **16** | `settings.storage.sub` | TR · Unresolved placeholder | An unresolved '{count}' placeholder is shown instead of the number ('1.2 GB ጥቅም ላይ ውሏል • 48.6 GB ነፃ'). |
| **13** | `settings.datasaver` | LY · Text runs off-screen | 'ውሂብ ቆጣቢ' runs off the edge of the screen. |

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
