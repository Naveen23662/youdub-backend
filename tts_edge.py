import edge_tts
import asyncio

# Voice mapping for 10 Indian languages
VOICE_MAP = {
    "en": "en-IN-PrabhatNeural",
    "hi": "hi-IN-MadhurNeural",
    "te": "te-IN-MohanNeural",
    "ta": "ta-IN-ValluvarNeural",
    "kn": "kn-IN-GaganNeural",
    "gu": "gu-IN-NiranjanNeural",
    "ml": "ml-IN-MidhunNeural",
    "mr": "mr-IN-ManoharNeural",
    "bn": "bn-IN-TusharNeural",
    "pa": "pa-IN-DeepNeural"
}

async def _synthesize(text, language_code, output_path):
    voice = VOICE_MAP.get(language_code)
    if not voice:
        raise ValueError(f"Unsupported language code: {language_code}")

    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_path)

def synthesize_speech(text, language_code, output_path):
    asyncio.run(_synthesize(text, language_code, output_path))

