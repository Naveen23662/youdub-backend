from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "YouDub is Live!"

@app.route("/translate")
def translate():
    text = request.args.get("text")
    lang = request.args.get("lang")
    return f"Translated: {text} to {lang}"

@app.route("/dub")
def dub():
    url = request.args.get("url")
    lang = request.args.get("lang")
    return f"YouTube URL: {url} | Target Language: {lang}"

