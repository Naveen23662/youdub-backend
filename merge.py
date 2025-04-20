from gtts import gTTS

def generate_dubbed_audio(text, lang_code):
    output_path = "static/downloads/output.mp3"
    tts = gTTS(text, lang=lang_code)
    tts.save(output_path)
    return output_path

