import requests

# Add supported languages here
LANG_CODE_MAP = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Punjabi": "pa"
}

def translate_text_libre(original_text, target_language):
    if target_language not in LANG_CODE_MAP:
        raise ValueError("Unsupported target language")

    target_code = LANG_CODE_MAP[target_language]
    url = "https://libretranslate.de/translate"
    payload = {
        "q": original_text,
        "source": "auto",
        "target": target_code,
        "format": "text"
    }

    try:
        response = requests.post(url, json=payload)
        return response.json()["translatedText"]
    except:
        raise RuntimeError("LibreTranslate failed")

