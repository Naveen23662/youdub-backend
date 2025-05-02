import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    try:
        print("Transcribing...")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print("❌ Transcription failed:", str(e))
        return None

