from typing import Protocol


class ExtractPolarityAndSensitivity(Protocol):

    def get_polarity(self, text: str) -> float:
        ...

    def get_sensitivity(self, text: str) -> float:
        ...
