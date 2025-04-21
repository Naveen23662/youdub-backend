from flask import Flask, request
from pytube import YouTube
import os
import whisper
from googletrans import Translator
import uuid

app = Flask(__name__)
model = whisper.load_model("base")
translator = Translator()

@app.route('/')
def home():
    return 'YouDub Flask App is working!'

@app.route('/translate')
def translate_text():
    text = request.args.get('text')
    lang = request.args.get('lang')
    translated = translator.translate(text, dest=lang)
    return f"Translated: {translated.text}"

@app.route('/dub', methods=['GET'])
def dub_youtube():
    url = request.args.get('url')
    lang = request.args.get('lang', 'hi')  # default to Hindi
    if not url:
        return "Missing URL", 400

    # Step 1: Download audio
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    filename = f"{uuid.uuid4()}.mp4"
    audio_stream.download(filename=filename)

    # Step 2: Transcribe using Whisper
    result = model.transcribe(filename)
    os.remove(filename)  # clean up
    text = result['text']

    # Step 3: Translate using Googletrans
    translated = translator.translate(text, dest=lang)
    return f"Translated Text: {translated.text}"

from flask import Flask, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/dub')
def dub():
    youtube_url = request.args.get('url')
    lang = request.args.get('lang')

    if not youtube_url or not lang:
        return "Missing YouTube URL or language code", 400

    # For now, just return a test message
    return f"YouTube URL: {youtube_url} | Target Language: {lang}"

