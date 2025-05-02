from flask import Flask, request, render_template, send_file
from downloader import download_audio_from_youtube
from translate_libre import translate_text_libre, LANG_CODE_MAP
from tts_edge import synthesize_speech
import tempfile
import whisper
import asyncio
import os

app = Flask(__name__)

# Whisper model (tiny or base for Render; medium or large locally)
model = whisper.load_model("base")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dub", methods=["POST"])
def dub():
    url = request.form.get("url")
    target_language = request.form.get("language")

    if not url or not target_language:
        return "Error: Please provide both URL and target language."

    print("Downloading audio...")
    audio_path = download_audio_from_youtube(url)
    if audio_path is None:
        return "Error: Could not download audio from YouTube."

    print("Transcribing...")
    try:
        result = model.transcribe(audio_path)
        original_text = result["text"]
    except Exception as e:
        return f"Error during transcription: {e}"

    print("Translating...")
    try:
        translated_text = translate_text_libre(original_text, target_language)
    except Exception as e:
        return f"Error during translation: {e}"

    print("Synthesizing speech...")
    try:
        output_path = "static/output.mp3"
        lang_code = LANG_CODE_MAP.get(target_language, "en")
        asyncio.run(synthesize_speech(translated_text, lang_code, output_path))
    except Exception as e:
        return f"Error during voice synthesis: {e}"

    return f"""
    <h2>Translation and Dubbing Complete</h2>
    <p><strong>Original:</strong> {original_text}</p>
    <p><strong>Translated:</strong> {translated_text}</p>
    <audio controls>
      <source src="/static/output.mp3" type="audio/mpeg">
      Your browser does not support the audio tag.
    </audio>
    <br><br>
    <a href="/static/output.mp3" download>Download Dubbed Audio</a>
    """

if __name__ == "__main__":
    app.run(debug=True)

