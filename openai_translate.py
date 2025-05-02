import requests

SUPPORTED_LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr"
}

def translate_text_openai(text, target_language):
    if target_language not in SUPPORTED_LANGUAGES:
        raise ValueError("Unsupported target language")

    target_code = SUPPORTED_LANGUAGES[target_language]

    response = requests.post("https://libretranslate.com/translate", json={
        "q": text,
        "source": "en",
        "target": target_code,
        "format": "text"
    })

    if response.status_code != 200:
        raise RuntimeError("LibreTranslate failed")

    return response.json()["translatedText"]

