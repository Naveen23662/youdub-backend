from faster_whisper import WhisperModel

def transcribe_audio(file_path):
    model = WhisperModel("base", compute_type="int8")
    segments, _ = model.transcribe(file_path)

    text = ""
    for segment in segments:
        text += segment.text
    return text.strip()

