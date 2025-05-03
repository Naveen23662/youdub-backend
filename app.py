from flask import Flask, render_template, request
from downloader import download_audio_from_youtube
from translate_libre import LANG_CODE_MAP, translate_text_libre
from tts_edge import synthesize_speech
from faster_whisper import WhisperModel
import os

app = Flask(__name__)

# --- Step 2 Transcription Function ---
def transcribe_audio(audio_path):
    try:
        # Load faster-whisper model with low memory footprint
        model = WhisperModel("base", compute_type="int8")

        # Transcribe the audio
        segments, info = model.transcribe(audio_path)

        # Combine all the segments
        result_text = " ".join(segment.text for segment in segments)
        return result_text

    except Exception as e:
        return f"Error during transcription: {str(e)}"

# --- Main Route ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Dubbing Route ---
@app.route('/dub', methods=['POST'])
def dub():
    try:
        url = request.form['url']
        target_lang = request.form['language']
        print("Downloading audio...")

        audio_path = download_audio_from_youtube(url)

        print("Transcribing...")
        text = transcribe_audio(audio_path)

        print("Translating...")
        translated_text = translate_text_libre(text, target_lang)

        print("Synthesizing speech...")
        output_path = synthesize_speech(translated_text, target_lang)

        return f"""
            <h2>Translated and Dubbed!</h2>
            <p><b>Original Text:</b> {text}</p>
            <p><b>Translated:</b> {translated_text}</p>
            <audio controls src="/{output_path}" autoplay></audio>
            <br><a href="/">Go back</a>
        """

    except Exception as e:
        return f"<p><b>Error:</b> {str(e)}</p>"

# --- Static file serving ---
@app.route('/output/<path:filename>')
def serve_audio(filename):
    return app.send_static_file(os.path.join('output', filename))

if __name__ == '__main__':
    app.run(debug=True)

