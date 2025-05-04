from flask import Flask, render_template, request, send_file
import os
import yt_dlp
import whisper
import asyncio
import edge_tts
from deep_translator import GoogleTranslator

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Function to generate dubbed audio using Edge TTS
async def generate_edge_tts(text, lang_code, gender, output_file):
    female_voices = {
        "en": "en-US-JennyNeural",
        "hi": "hi-IN-SwaraNeural",
        "te": "te-IN-ShrutiNeural",
        "ta": "ta-IN-PallaviNeural",
        "kn": "kn-IN-SapnaNeural",
        "ml": "ml-IN-SobhanaNeural",
        "mr": "mr-IN-KusumNeural",
        "gu": "gu-IN-DhwaniNeural",
        "bn": "bn-IN-TanishaaNeural",
        "pa": "pa-IN-PallaviNeural",
        "ur": "ur-PK-UzmaNeural",
        "fr": "fr-FR-DeniseNeural",
        "es": "es-ES-ElviraNeural"
    }

    male_voices = {
        "en": "en-US-GuyNeural",
        "hi": "hi-IN-MadhurNeural",
        "te": "te-IN-MohanNeural",
        "ta": "ta-IN-ValluvarNeural",
        "kn": "kn-IN-GaganNeural",
        "ml": "ml-IN-MidhunNeural",
        "mr": "mr-IN-AaravNeural",
        "gu": "gu-IN-NiranjanNeural",
        "bn": "bn-IN-TanishNeural",
        "pa": "pa-IN-JagjitNeural",
        "ur": "ur-PK-AsadNeural",
        "fr": "fr-FR-HenriNeural",
        "es": "es-ES-AlvaroNeural"
    }

    if gender == "female":
        voice = female_voices.get(lang_code, "en-US-JennyNeural")
    else:
        voice = male_voices.get(lang_code, "en-US-GuyNeural")

    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_file)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")
        target_language = request.form.get("language")
        voice_gender = request.form.get("gender")

        if not youtube_url or not target_language:
            return "Missing YouTube URL or language", 400

        try:
            # Step 1: Download YouTube audio
            output_path = os.path.join(DOWNLOAD_FOLDER, "original_audio.%(ext)s")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])

            # Step 2: Transcribe using Whisper
            model = whisper.load_model("base")
            downloaded_mp3 = os.path.join(DOWNLOAD_FOLDER, "original_audio.mp3")
            result = model.transcribe(downloaded_mp3, fp16=False)
            english_text = result["text"]

            # Step 3: Translate text
            translated_text = GoogleTranslator(source='en', target=target_language).translate(english_text)

            # Step 4: Dub using Edge TTS
            dubbed_path = os.path.join(DOWNLOAD_FOLDER, "dubbed_audio.mp3")
            asyncio.run(generate_edge_tts(translated_text, target_language, voice_gender, dubbed_path))

            return send_file(dubbed_path, as_attachment=True)

        except Exception as e:
            return f"Error processing video: {e}", 500

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

