from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "YouDub backend is live!"

@app.route('/dub', methods=['POST'])
def dub():
    data = request.json
    text = data.get("text")
    target_lang = data.get("lang")

    if not text or not target_lang:
        return jsonify({"error": "Missing text or target language"}), 400

    try:
        model_map = {
            "hi": "Helsinki-NLP/opus-mt-en-hi",
            "te": "Helsinki-NLP/opus-mt-en-te",
            "ta": "Helsinki-NLP/opus-mt-en-ta",
            "kn": "Helsinki-NLP/opus-mt-en-kn",
            "ml": "Helsinki-NLP/opus-mt-en-ml",
            "mr": "Helsinki-NLP/opus-mt-en-mr",
            "bn": "Helsinki-NLP/opus-mt-en-bn",
            "gu": "Helsinki-NLP/opus-mt-en-gu",
            "pa": "Helsinki-NLP/opus-mt-en-pa",
            "es": "Helsinki-NLP/opus-mt-en-es",
            "fr": "Helsinki-NLP/opus-mt-en-fr",
            "de": "Helsinki-NLP/opus-mt-en-de",
            "it": "Helsinki-NLP/opus-mt-en-it",
            "ja": "Helsinki-NLP/opus-mt-en-ja",
            "ko": "Helsinki-NLP/opus-mt-en-ko",
            "zh": "Helsinki-NLP/opus-mt-en-zh",
            "ru": "Helsinki-NLP/opus-mt-en-ru",
            "pt": "Helsinki-NLP/opus-mt-en-pt",
            "ar": "Helsinki-NLP/opus-mt-en-ar"
        }

        model_id = model_map.get(target_lang)
        if not model_id:
            return jsonify({"error": f"Language '{target_lang}' not supported"}), 400

        translator = pipeline("translation", model=model_id)
        result = translator(text, max_length=512)

        return jsonify({
            "message": "✅ Translation successful",
            "translated": result[0]['translation_text'],
            "lang": target_lang
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

