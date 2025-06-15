kfrom flask import Flask, request, send_file
from flask_cors import CORS
from transformers import MarianMTModel, MarianTokenizer
import torch
import asyncio
import edge_tts

app = Flask(__name__)
CORS(app)

# Language code map
lang_model_map = {
    "hi": "Helsinki-NLP/opus-mt-en-hi",
    "te": "Helsinki-NLP/opus-mt-en-te",
    "ta": "Helsinki-NLP/opus-mt-en-ta",
    "ml": "Helsinki-NLP/opus-mt-en-ml",
    "kn": "Helsinki-NLP/opus-mt-en-kn",
    "mr": "Helsinki-NLP/opus-mt-en-mr",
    "bn": "Helsinki-NLP/opus-mt-en-bn",
    "gu": "Helsinki-NLP/opus-mt-en-gu",
    "pa": "Helsinki-NLP/opus-mt-en-pa",
    "ur": "Helsinki-NLP/opus-mt-en-ur",
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "it": "Helsinki-NLP/opus-mt-en-it",
    "ru": "Helsinki-NLP/opus-mt-en-ru",
    "zh": "Helsinki-NLP/opus-mt-en-zh",
    "ja": "Helsinki-NLP/opus-mt-en-jap",
    "ko": "Helsinki-NLP/opus-mt-en-ko",
    "pt": "Helsinki-NLP/opus-mt-en-pt",
    "ar": "Helsinki-NLP/opus-mt-en-ar",
    "en": None  # English — no translation needed
}

# Translation function
def translate(text, lang_code):
    if lang_code == "en":
        return text
    model_name = lang_model_map.get(lang_code)
    if not model_name:
        return "Unsupported language"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# TTS function
async def generate_audio(text, lang_code, filename):
    voice_map = {
        "hi": "hi-IN-SwaraNeural", "te": "te-IN-MohanNeural", "ta": "ta-IN-PallaviNeural",
        "ml": "ml-IN-SobhanaNeural", "kn": "kn-IN-GaganNeural", "mr": "mr-IN-AarohiNeural",
        "bn": "bn-IN-TanishaaNeural", "gu": "gu-IN-DhwaniNeural", "pa": "pa-IN-IpseetaNeural",
        "ur": "ur-IN-GulNeural", "en": "en-IN-PrabhatNeural", "fr": "fr-FR-DeniseNeural",
        "de": "de-DE-KatjaNeural", "es": "es-ES-ElviraNeural", "it": "it-IT-ElsaNeural",
        "ru": "ru-RU-DariyaNeural", "zh": "zh-CN-XiaoxiaoNeural", "ja": "ja-JP-NanamiNeural",
        "ko": "ko-KR-SunHiNeural", "pt": "pt-BR-FranciscaNeural", "ar": "ar-EG-SalmaNeural"
    }
    voice = voice_map.get(lang_code, "en-IN-PrabhatNeural")
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

@app.route("/dub", methods=["POST"])
def dub():
    data = request.json
    text = data.get("text")
    lang = data.get("lang", "en")
    translated = translate(text, lang)
    filename = "dubbed.mp3"
    asyncio.run(generate_audio(translated, lang, filename))
    return send_file(filename, mimetype="audio/mpeg")

