from flask import Flask, request

app = Flask(__name__)

@app.route('/dub')
def dub():
    youtube_url = request.args.get('url')
    target_lang = request.args.get('lang')

    if not youtube_url or not target_lang:
        return "Missing YouTube URL or target language", 400

    return f"YouTube URL received: {youtube_url} | Target Language: {target_lang}"

