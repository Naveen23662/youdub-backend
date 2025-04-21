from googletrans import Translator

def translate_text(text, lang):
    translator = Translator()
    result = translator.translate(text, dest=lang)
    return result.text

