from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'YouDub Backend Running'})

@app.route('/dub', methods=['POST'])
def dub():
    data = request.get_json()
    youtube_url = data.get('youtube_url')
    language = data.get('language')

    # Simulate processing
    if youtube_url and language:
        return jsonify({'status': 'success', 'message': f'Dubbing {youtube_url} to {language}'})
    else:
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

if __name__ == '__main__':
    app.run(debug=True)

