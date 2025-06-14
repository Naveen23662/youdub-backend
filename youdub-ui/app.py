from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

@app.route('/')
def home():
    return "YouDub backend is live!"

@app.route('/dub', methods=['POST'])
def dub():
    data = request.json
    youtube_url = data.get("url")
    target_lang = data.get("lang")

    if not youtube_url or not target_lang:
        return jsonify({"error": "Missing YouTube URL or language"}), 400

    # Temporary response until dubbing pipeline is added
    return jsonify({
        "message": "✅ Received your request!",
        "url": youtube_url,
        "target_lang": target_lang
    })

