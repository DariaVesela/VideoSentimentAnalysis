from videosentimentanalysis.usecases.protocols.translate_text import TranslateText, LanguageOptions
from deep_translator import GoogleTranslator

class TextTranslation(TranslateText):

    def translate_text(self, text: str, source_lang:LanguageOptions, target_lang:LanguageOptions) -> str:
        translated = GoogleTranslator(source=source_lang.value.lower(), target=target_lang.value.lower()).translate(text)
        return translated


