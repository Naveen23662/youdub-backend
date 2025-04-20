from flask import Flask, render_template, request, send_from_directory
import os
from downloader import download_audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    youtube_url = request.form.get('youtube_url')
    language = request.form.get('language')

    if not youtube_url:
        return "⚠️ Error: No YouTube URL provided.", 400

    audio_path = download_audio(youtube_url)  # only one argument now

    if not audio_path or not os.path.exists(audio_path):
        return render_template('error.html', error="No audio file found.")

    return render_template(
        'success.html',
        youtube_url=youtube_url,
        audio_path=audio_path,
        video_path="outputs/final_dubbed_video.mp4"
    )

@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename)

@app.route('/outputs/<path:filename>')
def download_output_file(filename):
    return send_from_directory('outputs', filename)

if __name__ == '__main__':
    app.run(debug=True)

