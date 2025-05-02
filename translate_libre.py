import requests

# Supported language codes (ISO 639-1)
SUPPORTED_LANGUAGES = [
    "en",  # English
    "hi",  # Hindi
    "te",  # Telugu
    "ta",  # Tamil
    "kn",  # Kannada
    "gu",  # Gujarati
    "ml",  # Malayalam
    "mr",  # Marathi
    "bn",  # Bengali
    "pa",  # Punjabi
]

# Display name for dropdown in index.html
LANG_CODE_MAP = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Punjabi": "pa",
}

def translate_text_libre(text, target_lang):
    if target_lang not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported target language")

    print("Translating...")

    response = requests.post(
        "https://libretranslate.com/translate",
        headers={"Content-Type": "application/json"},
        json={
            "q": text,
            "source": "en",
            "target": target_lang,
            "format": "text"
        }
    )

    if response.status_code == 200:
        return response.json()["translatedText"]
    else:
        raise RuntimeError("LibreTranslate failed")

