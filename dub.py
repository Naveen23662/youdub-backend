# dub.py
from pytube import YouTube

def download_audio(youtube_url):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_path = "static/downloads"
    filename = "dubbed.mp3"
    audio_stream.download(output_path=output_path, filename=filename)

