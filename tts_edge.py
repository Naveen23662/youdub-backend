import edge_tts
import asyncio

VOICE_MAP = {
    "en": "en-IN-PrabhatNeural",
    "hi": "hi-IN-MadhurNeural",
    "te": "te-IN-MohanNeural",
    "ta": "ta-IN-ValluvarNeural",
    "kn": "kn-IN-GaganNeural",
    "ml": "ml-IN-MidhunNeural",
    "bn": "bn-BD-PradeepNeural",
    "gu": "gu-IN-NiranjanNeural",
    "mr": "mr-IN-ManoharNeural",
    "pa": "pa-IN-ManpreetNeural"
}

async def synthesize_speech(text, lang_code, output_path="output.mp3"):
    voice = VOICE_MAP.get(lang_code, "en-IN-PrabhatNeural")
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_path)

