from flask import Flask, request
from dub import process_dubbing

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to YouDub!"

@app.route('/dub')
def dub_video():
    youtube_url = request.args.get('url')
    target_language = request.args.get('lang')

    # Run dummy dubbing and get audio path
    output_path = process_dubbing(youtube_url, target_language)

    return f'''
    <h3>Dubbed Audio Created ✅</h3>
    <p>URL: {youtube_url}</p>
    <p>Language: {target_language}</p>
    <audio controls src="/{output_path}"></audio><br>
    <a href="/{output_path}" download>Download Dubbed Audio</a>
    '''

