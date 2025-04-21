from flask import send_file

@app.route("/dub")
def dub():
    url = request.args.get("url")
    lang = request.args.get("lang")

    # 👇 Step 1: Download audio from YouTube and save as input.mp3
    from pytube import YouTube
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path="static/downloads", filename="input.mp3")

    # 👇 Step 2: Dummy dubbing (you can replace this with real Whisper/voice clone)
    import shutil
    output_path = f"static/downloads/output_{lang}.mp3"
    shutil.copy("static/downloads/input.mp3", output_path)

    # 👇 Step 3: Send dubbed file back
    return send_file(output_path, as_attachment=True)

