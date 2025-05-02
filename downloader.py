import yt_dlp
import numpy as np
import tempfile

def download_audio_from_youtube(url):
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': temp_audio.name,
                'quiet': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            return temp_audio.name
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None

