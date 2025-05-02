import asyncio
from tts_edge import tts_edge

def synthesize_speech(text, lang_code):
    output_file = f"static/output_{lang_code}.mp3"
    asyncio.run(tts_edge(text, lang_code, output_file))
    return output_file

