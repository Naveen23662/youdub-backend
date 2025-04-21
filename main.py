from flask import Flask, request, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/dub')
def dub():
    youtube_url = request.args.get("url")
    lang = request.args.get("lang")

    return render_template_string("""
    <h2>YouTube URL: {{ youtube_url }} | Target Language: {{ lang }}</h2>
    <audio controls>
      <source src="/static/downloads/dubbed.mp3" type="audio/mpeg">
      Your browser does not support the audio element.
    </audio>
    <br>
    <a href="/static/downloads/dubbed.mp3" download>Download Dubbed Audio</a>
    """, youtube_url=youtube_url, lang=lang)

