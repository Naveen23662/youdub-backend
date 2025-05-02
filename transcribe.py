from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel("tiny", compute_type="int8")  # very light model
    segments, _ = model.transcribe(audio_path)
    return " ".join([segment.text for segment in segments])

