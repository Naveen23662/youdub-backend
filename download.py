import os
import yt_dlp

def download_audio(youtube_url):
    output_folder = "static/downloads"
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=True)
        file_id = info_dict.get("id", "")
        output_path = f"{output_folder}/{file_id}.mp3"

        # Check if file was saved
        if not os.path.exists(output_path):
            raise FileNotFoundError(f"MP3 not found at: {output_path}")

        return output_path

