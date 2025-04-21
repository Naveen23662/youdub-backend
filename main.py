from flask import Flask, request, send_file
from downloader import download_audio
from dubber import dummy_dub

app = Flask(__name__)

@app.route('/dub')
def dub_video():
    url = request.args.get('url')
    lang = request.args.get('lang')

    # Step 1: Download YouTube audio
    audio_path = download_audio(url)

    # Step 2: Dummy dubbing (can replace with Whisper later)
    dubbed_path = dummy_dub(audio_path, lang)

    # Step 3: Send file to user
    return send_file(dubbed_path, as_attachment=True)

