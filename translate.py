# translate.py
from googletrans import Translator

def translate_text(text, target_lang):
    translator = Translator()
    result = translator.translate(text, dest=target_lang)
    return result.text

