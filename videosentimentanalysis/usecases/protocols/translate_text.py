from enum import StrEnum
from typing import Protocol

class LanguageOptions(StrEnum):
    ENGLISH = "EN"
    SPANISH = "ES"


class TranslateText(Protocol):

    def translate_text(self, text: str, source_lang:LanguageOptions, target_lang:LanguageOptions) -> str:
        ...

