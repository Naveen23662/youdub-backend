from gtts import gTTS

# Load translated text
with open("outputs/translated.txt", "r", encoding="utf-8") as f:
    translated_text = f.read()

# Convert to speech
tts = gTTS(text=translated_text, lang="te")  # "te" for Telugu; change to "hi" for Hindi

# Save audio
tts.save("outputs/dubbed.mp3")

print("✅ Dubbed audio saved to outputs/dubbed.mp3")

