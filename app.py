from flask import Flask, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/")
def index():
    return "YouDub Flask App is working!"

@app.route("/translate")
def translate():
    text = request.args.get("text", default="Hello", type=str)
    dest = request.args.get("lang", default="te", type=str)  # Telugu by default
    translated = translator.translate(text, dest=dest)
    return f"Translated: {translated.text}"

# Example: https://yourapp.onrender.com/translate?text=hello&lang=te

