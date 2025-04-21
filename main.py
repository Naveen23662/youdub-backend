from flask import Flask, request, send_file
from pytube import YouTube
from translate import translate_text
from dub import generate_dub
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "YouDub is live!"

@app.route("/translate")
def translate():
    text = request.args.get("text", "")
    lang = request.args.get("lang", "")
    translated = translate_text(text, lang)
    return f"Translated: {translated}"

@app.route("/dub")
def dub_video():
    youtube_url = request.args.get("url")
    lang = request.args.get("lang")

    if not youtube_url or not lang:
        return "Missing parameters", 400

    try:
        print("Downloading audio...")
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True).first()
        download_path = "static/downloads/input.mp3"
        stream.download(filename=download_path)

        print("Generating dub...")
        dubbed_path = generate_dub(download_path, lang)

        print("Sending file back...")
        return send_file(dubbed_path, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}", 500

