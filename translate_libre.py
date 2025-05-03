from deep_translator import LibreTranslator

# Language code map for display purposes
LANG_CODE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "kn": "Kannada",
    "mr": "Marathi",
    "ml": "Malayalam",
    "gu": "Gujarati",
    "bn": "Bengali",
    "pa": "Punjabi"
}

def translate_text_libre(text, target_lang):
    try:
        translated = LibreTranslator(source="auto", target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation failed: {str(e)}"

