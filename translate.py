from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        return f"❌ Translation error: {str(e)}"

