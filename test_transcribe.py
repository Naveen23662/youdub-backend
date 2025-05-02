from transcribe import download_audio, transcribe_audio
from translate import translate_text

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
target_language = "te"  # Telugu (hi = Hindi, ta = Tamil, etc.)

# 1. Download & Transcribe
print("Downloading and transcribing...")
mp3_path = download_audio(url)
text = transcribe_audio(mp3_path)

# 2. Translate
translated = translate_text(text, target_language)

# 3. Output
print("\n✅ ORIGINAL:")
print(text)
print("\n🌍 TRANSLATED:")
print(translated)

