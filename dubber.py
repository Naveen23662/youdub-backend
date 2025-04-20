import whisper
from gtts import gTTS
from googletrans import Translator

# Load Whisper model
model = whisper.load_model("base")

# Transcribe audio
audio_path = "static/downloads/Gold Coins falling animation green screen Effects with sounds HD video.mp3"
result = model.transcribe(audio_path)
original_text = result["text"]
print("Original Text:", original_text)

# Translate text
target_lang = "hi"  # hi = Hindi, te = Telugu, fr = French, etc.
translator = Translator()
translated = translator.translate(original_text, dest=target_lang)
translated_text = translated.text
print("Translated:", translated_text)

# Convert translated text to speech
tts = gTTS(translated_text, lang=target_lang)
tts.save("static/dubbed_audio.mp3")
print("Dubbed audio saved!")

