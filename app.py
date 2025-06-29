
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "YouDub backend is live!"})

@app.route("/dub", methods=["POST"])
def dub_video():
    data = request.json
    video_url = data.get("url")
    target_language = data.get("language")
    # This is a placeholder logic
    return jsonify({
        "status": "success",
        "message": f"Dubbing started for {video_url} in {target_language}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

