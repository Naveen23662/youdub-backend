@app.route('/dub')
def dub():
    youtube_url = request.args.get('url')
    target_lang = request.args.get('lang')

    # Logging input for debug
    print("Received:", youtube_url, "|", target_lang)

    return f"""
    <h3>YouTube URL: {youtube_url} | Target Language: {target_lang}</h3>
    <audio controls>
        <source src="/static/downloads/dubbed.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <br>
    <a href="/static/downloads/dubbed.mp3" download>Download Dubbed Audio</a>
    """

