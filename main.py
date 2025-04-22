# main.py
from flask import Flask, request, render_template_string
from dub import download_audio

app = Flask(__name__)

@app.route("/dub")
def dub_video():
    url = request.args.get("url")
    lang = request.args.get("lang", "en")

    if not url:
        return "Missing YouTube URL", 400

    try:
        download_audio(url)
        audio_path = "/static/downloads/dubbed.mp3"
        return render_template_string(f"""
            <h2>YouDub - Dubbed Audio</h2>
            <p><b>YouTube URL:</b> {url}</p>
            <p><b>Target Language:</b> {lang}</p>
            <audio controls>
                <source src="{audio_path}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio><br>
            <a href="{audio_path}" download>Download Dubbed Audio</a>
        """)
    except Exception as e:
        return f"❌ Error occurred: {str(e)}", 500

if __name__ == "__main__":
    app.run()

