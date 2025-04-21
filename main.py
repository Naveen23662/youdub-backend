from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route("/dub")
def dub_audio():
    url = request.args.get("url")
    lang = request.args.get("lang")

    # Just simulating output path (adjust this as per your actual dubbing logic)
    dubbed_path = f"static/downloads/output_{lang}.mp3"

    if os.path.exists(dubbed_path):
        return send_file(dubbed_path, as_attachment=True)
    else:
        return f"Dubbed audio not found at {dubbed_path}", 404

