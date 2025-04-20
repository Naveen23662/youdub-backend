import whisper
import os

# Load Whisper model
model = whisper.load_model("base")

# Transcribe the audio
result = model.transcribe("downloads/audio.mp3")

# Save the text
with open("outputs/transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcription saved to outputs/transcription.txt")

