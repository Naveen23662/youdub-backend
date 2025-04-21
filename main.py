from flask import Flask, request, send_file
from pytube import YouTube
from translate import translate_text
from dub import generate_dub
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "YouDub is running!"

@app.route("/translate")
def translate():
    text = request.args.get("text", "")
    lang = request.args.get("lang", "")
    translated = translate_text(text, lang)
    return f"Translated: {translated}"

@app.route("/dub")
def dub():
    try:
        url = request.args.get("url")
        lang = request.args.get("lang")

        if not url or not lang:
            return "Missing URL or language", 400

        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        input_path = "static/downloads/input.mp3"
        stream.download(filename=input_path)

        output_path = generate_dub(input_path, lang)

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}", 500

