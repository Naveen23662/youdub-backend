from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "YouDub Flask is running!"

@app.route('/dub')
def dub():
    language = request.args.get('language')
    video_url = request.args.get('video')
    
    return f"""
    <h2>YouDub - Dubbing in {language}</h2>
    <p>Video URL: {video_url}</p>
    """
    
if __name__ == '__main__':
    app.run(debug=True)

