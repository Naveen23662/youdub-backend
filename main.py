from flask import Flask, request
from dub import process_dubbing

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to YouDub!"

@app.route('/dub')
def dub_video():
    url = request.args.get('url')
    lang = request.args.get('lang')

    # Step 1: Download YouTube audio
    audio_path = download_audio(url)

    # Step 2: Translate + dub (dummy now, real logic later)
    dubbed_path = dummy_dub(audio_path, lang)

    # Step 3: Serve the dubbed file
    return send_file(dubbed_path, as_attachment=True)

