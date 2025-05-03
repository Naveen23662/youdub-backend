import edge_tts
import asyncio
import os
import uuid

# Helper to pick a voice based on language
VOICE_MAP = {
    "en": "en-US-AriaNeural",
    "hi": "hi-IN-SwaraNeural",
    "te": "te-IN-MohanNeural",
    "ta": "ta-IN-PallaviNeural",
    "kn": "kn-IN-GaganNeural",
    "mr": "mr-IN-AarohiNeural",
    "ml": "ml-IN-SobhanaNeural",
    "gu": "gu-IN-DhwaniNeural",
    "bn": "bn-IN-TanishaaNeural",
    "pa": "pa-IN-SonalNeural"
}

async def generate_tts(text, lang_code, output_path):
    voice = VOICE_MAP.get(lang_code, "en-US-AriaNeural")
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_path)

def synthesize_speech(text, lang_code):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{uuid.uuid4()}.mp3"
    asyncio.run(generate_tts(text, lang_code, filename))
    return filename

