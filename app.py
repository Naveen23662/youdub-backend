from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os
import uuid

app = Flask(__name__)
CORS(app)

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

    # Generate temp filename
    out_file = f"audio_{uuid.uuid4().hex}.mp3"

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': out_file,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        return jsonify({
            "message": "✅ Audio downloaded",
            "file": out_file,
            "lang": target_lang
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

