import yt_dlp
import os

def download_audio_from_youtube(url):
    try:
        output_path = "static/input_audio.mp3"
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print("✅ Downloaded:", info['title'])

        return output_path

    except Exception as e:
        print("❌ Download failed:", str(e))
        return None

