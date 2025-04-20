from flask import Flask, render_template, request, send_file
import os
from download_video import download_audio
from transcribe import transcribe_audio
from translate import translate_text
from merge import generate_dubbed_audio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        language = request.form["language"]

        try:
            input_path = download_audio(url)  # Downloads and returns path to MP3
            transcript = transcribe_audio(input_path)  # Transcribe to text
            translated_text = translate_text(transcript, language)  # Translate
            dubbed_path = generate_dubbed_audio(translated_text, language)  # Generate new mp3

            return render_template("index.html", success=True, transcript=transcript, translated=translated_text)
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

@app.route("/download")
def download():
    dubbed_path = "static/downloads/output.mp3"
    if os.path.exists(dubbed_path):
        return send_file(dubbed_path, as_attachment=True)
    return "Dubbed file not found.", 404

if __name__ == "__main__":
    app.run(debug=True)

