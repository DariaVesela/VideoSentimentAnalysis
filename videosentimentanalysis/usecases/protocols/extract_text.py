from typing import Protocol

from videosentimentanalysis.domain.audio import Audio

class ExtractText(Protocol):
    def get_text(self, audio: Audio) -> str:
        ...