from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel("base", compute_type="int8")  # use int8 to save memory
    segments, info = model.transcribe(audio_path)

    full_text = ""
    for segment in segments:
        full_text += segment.text
    return full_text.strip()

