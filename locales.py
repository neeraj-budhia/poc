"""Locale support table for the localization-check engine.

Source of truth: "Spotify's 73 Languages" tab of the Localization Test Bed
sheet (1a-PlMT6p12IYyeqkSOwtWQhok5sV3dknpHwe_pFONl4, gid 526335473) —
the customer's full target list. Columns: Smartling code, reading direction.

The engine is language-agnostic (one v8 prompt); what varies per locale is
(a) reading direction — drives the geometry stage's RTL mirror normalization,
(b) reasoning-effort routing — full effort for RTL scripts (measured: low
    effort costs 7+ recall points on Arabic and the hybrid does not
    compensate; every other validated language is flat-to-better on low),
(c) which script family a locale belongs to — drives the validation plan
    (one representative testbed per family, not per locale).
"""

RTL_CODES = {"ar", "ar-EG", "ar-MA", "ar-SA", "he-IL", "fa-IR", "pa-PK", "ur"}

# Smartling code -> (display name, script family)
LOCALES = {
    "af-ZA": ("Afrikaans (South Africa)", "latin"),
    "am-ET": ("Amharic (Ethiopia)", "ethiopic"),
    "ar-EG": ("Arabic (Egypt)", "arabic"),
    "ar":    ("Arabic (International)", "arabic"),
    "ar-MA": ("Arabic (Morocco)", "arabic"),
    "ar-SA": ("Arabic (Saudi Arabia)", "arabic"),
    "az-AZ": ("Azerbaijani (Azerbaijan)", "latin"),
    "eu-ES": ("Basque (Spain)", "latin"),
    "bn-IN": ("Bengali (India)", "indic"),
    "bp":    ("Bhojpuri", "indic"),
    "bs-BA": ("Bosnian (Bosnia and Herzegovina)", "latin"),
    "bg-BG": ("Bulgarian (Bulgaria)", "cyrillic"),
    "ca-ES": ("Catalan (Spain)", "latin"),
    "zh-CN": ("Chinese (China-Simplified)", "cjk"),
    "zh-HK": ("Chinese (Hong Kong)", "cjk"),
    "zh-TW": ("Chinese (Taiwan-Traditional)", "cjk"),
    "hr-HR": ("Croatian (Croatia)", "latin"),
    "cs-CZ": ("Czech (Czechia)", "latin"),
    "da-DK": ("Danish (Denmark)", "latin"),
    "nl-NL": ("Dutch (Netherlands)", "latin"),
    "en-GB": ("English (United Kingdom)", "latin"),
    "et-EE": ("Estonian (Estonia)", "latin"),
    "fp-PH": ("Filipino (Philippines)", "latin"),
    "fi-FI": ("Finnish (Finland)", "latin"),
    "fr-CA": ("French (Canada)", "latin"),
    "fr-FR": ("French (France)", "latin"),
    "gl-ES": ("Galician (Spain)", "latin"),
    "de-DE": ("German (Germany)", "latin"),
    "el-GR": ("Greek (Greece)", "greek"),
    "gu-IN": ("Gujarati (India)", "indic"),
    "he-IL": ("Hebrew (Israel)", "hebrew"),
    "hi-IN": ("Hindi (India)", "indic"),
    "hu-HU": ("Hungarian (Hungary)", "latin"),
    "is-IS": ("Icelandic (Iceland)", "latin"),
    "id-ID": ("Indonesian (Indonesia)", "latin"),
    "it-IT": ("Italian (Italy)", "latin"),
    "ja-JP": ("Japanese (Japan)", "cjk"),
    "kn-IN": ("Kannada (India)", "indic"),
    "ko-KR": ("Korean (South Korea)", "cjk"),
    "lv-LV": ("Latvian (Latvia)", "latin"),
    "lt-LT": ("Lithuanian (Lithuania)", "latin"),
    "mk-MK": ("Macedonian (North Macedonia)", "cyrillic"),
    "ms-MY": ("Malay (Malaysia)", "latin"),
    "ml-IN": ("Malayalam (India)", "indic"),
    "mr-IN": ("Marathi (India)", "indic"),
    "ne-NP": ("Nepali (Nepal)", "indic"),
    "nb-NO": ("Norwegian (Bokmål)", "latin"),
    "or-IN": ("Odia/Oriya (India)", "indic"),
    "fa-IR": ("Persian (Iran)", "arabic"),
    "pl-PL": ("Polish (Poland)", "latin"),
    "pt-BR": ("Portuguese (Brazil)", "latin"),
    "pt-PT": ("Portuguese (Portugal)", "latin"),
    "pa-IN": ("Punjabi (India)", "indic"),
    "pa-PK": ("Punjabi (Pakistan)", "arabic"),
    "ro-RO": ("Romanian (Romania)", "latin"),
    "ru-RU": ("Russian (Russia)", "cyrillic"),
    "sr-RS": ("Serbian (Serbia)", "cyrillic"),
    "sk-SK": ("Slovak (Slovakia)", "latin"),
    "sl-SI": ("Slovenian (Slovenia)", "latin"),
    "es-AR": ("Spanish (Argentina)", "latin"),
    "es-LA": ("Spanish (Latin America)", "latin"),
    "es-MX": ("Spanish (Mexico)", "latin"),
    "es-ES": ("Spanish (Spain)", "latin"),
    "sw":    ("Swahili (International)", "latin"),
    "sv-SE": ("Swedish (Sweden)", "latin"),
    "ta-IN": ("Tamil (India)", "indic"),
    "te-IN": ("Telugu (India)", "indic"),
    "th-TH": ("Thai (Thailand)", "thai"),
    "tr-TR": ("Turkish (Turkey)", "latin"),
    "uk-UA": ("Ukrainian (Ukraine)", "cyrillic"),
    "ur":    ("Urdu", "arabic"),
    "vi-VN": ("Vietnamese (Vietnam)", "latin"),
    "zu-ZA": ("Zulu (South Africa)", "latin"),
}

# script family -> the locale whose testbed validates it (None = untested)
FAMILY_VALIDATED_BY = {
    "latin": "de-DE",      # 176-defect grid; Percy + fixture corpora
    "cjk": "ja-JP",        # ShopEasy-v2 + DailyPost JA
    "arabic": "ar-SA",     # BankEasy + DailyPost AR (hybrid required)
    "indic": "hi-IN",      # DailyPost HI (Devanagari); other Indic scripts untested
    "hebrew": None, "cyrillic": None, "greek": None, "thai": None, "ethiopic": None,
}

_NAME_TO_CODE = {name.lower(): code for code, (name, _) in LOCALES.items()}


def resolve(target_lang: str) -> str | None:
    """Locale code for a target_lang string as the contract sends it —
    accepts a bare code ('ar-SA'), 'Language (code)' ('Arabic (ar-SA)'),
    or the sheet's display name ('Arabic (Saudi Arabia)')."""
    t = (target_lang or "").strip()
    if t in LOCALES:
        return t
    if "(" in t:
        inner = t[t.index("(") + 1:t.rindex(")")].strip()
        if inner in LOCALES:
            return inner
    low = t.lower()
    if low in _NAME_TO_CODE:
        return _NAME_TO_CODE[low]
    lang = low.split("(")[0].strip()
    for code, (name, _) in LOCALES.items():
        if name.lower().split("(")[0].strip() == lang:
            return code
    return None


def is_rtl(target_lang: str) -> bool:
    code = resolve(target_lang)
    if code:
        return code in RTL_CODES
    # conservative fallback for strings the table can't resolve
    t = (target_lang or "").lower()
    return any(k in t for k in ("arabic", "hebrew", "urdu", "persian", "ar-", "he-", "fa-", "ur"))


def reasoning_effort(target_lang: str) -> str:
    """Measured routing: RTL scripts need full effort; everything else low."""
    return "medium" if is_rtl(target_lang) else "low"
