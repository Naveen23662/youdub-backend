from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dub', methods=['POST'])
def dub():
    data = request.get_json()
    youtube_url = data.get('youtube_url')
    language = data.get('language')

    if youtube_url and language:
        return jsonify({'status': 'success', 'message': f'Dubbing {youtube_url} in {language}'})
    else:
        return jsonify({'status': 'error', 'message': 'Missing data'}), 400

if __name__ == '__main__':
    app.run(debug=True)

