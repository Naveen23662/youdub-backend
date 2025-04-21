from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/dub")
def dub_video():
    youtube_url = request.args.get("url")
    target_language = request.args.get("lang")

    # HTML Template with audio playback
    html_template = """
    <!DOCTYPE html>
    <html>
    <head><title>YouDub Output</title></head>
    <body>
        <h3>YouTube URL: {{ youtube_url }} | Target Language: {{ target_language }}</h3>
        <audio controls>
            <source src="/static/downloads/dubbed.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <br><br>
        <a href="/static/downloads/dubbed.mp3" download>Download Dubbed Audio</a>
    </body>
    </html>
    """

    return render_template_string(html_template, youtube_url=youtube_url, target_language=target_language)

