from flask import Flask, render_template, request
from downloader import download_audio_from_youtube
from transcribe import transcribe_audio
from translate_libre import translate_text_libre
from tts_edge import synthesize_speech

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dub", methods=["POST"])
def dub():
    try:
        url = request.form.get("url")
        language = request.form.get("language")

        print("🔍 URL received:", url)
        print("🌐 Target language:", language)

        # Step 1: Download audio
        audio_path = download_audio_from_youtube(url)
        if audio_path is None:
            return "Error: Audio download failed."

        print("🎧 Audio downloaded:", audio_path)

        # Step 2: Transcribe
        original_text = transcribe_audio(audio_path)
        print("✍️ Transcribed Text:", original_text)

        # Step 3: Translate
        translated_text = translate_text_libre(original_text, language)
        print("🌎 Translated Text:", translated_text)

        # Step 4: Synthesize speech
        output_path = "static/output.mp3"
        synthesize_speech(translated_text, language, output_path)

        return render_template("index.html", original_text=original_text,
                               translated_text=translated_text, audio_file=output_path)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

