from deep_translator import GoogleTranslator

# Load transcription text
with open("outputs/transcription.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Translate to desired language
target_language = "te"  # te for Telugu, hi for Hindi
translated = GoogleTranslator(source='auto', target=target_language).translate(text)

# Save translated text
with open("outputs/translated.txt", "w", encoding="utf-8") as f:
    f.write(translated)

print("✅ Translated text saved to outputs/translated.txt")

