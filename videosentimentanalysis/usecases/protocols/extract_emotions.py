from typing import Protocol


class ExtractEmotions(Protocol):

    def get_emotions(self, text:str) -> dict[str,int]:
        ...

