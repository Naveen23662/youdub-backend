from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "YouDub is Live"

@app.route("/dub")
def dub_video():
    youtube_url = request.args.get("url")
    target_language = request.args.get("lang")

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>YouDub</title></head>
    <body>
        <h2>YouTube URL: {{ youtube_url }} | Target Language: {{ target_language }}</h2>
        <audio controls>
            <source src="/static/downloads/dubbed.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <br><br>
        <a href="/static/downloads/dubbed.mp3" download>Download Dubbed Audio</a>
    </body>
    </html>
    """
    return render_template_string(html, youtube_url=youtube_url, target_language=target_language)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

