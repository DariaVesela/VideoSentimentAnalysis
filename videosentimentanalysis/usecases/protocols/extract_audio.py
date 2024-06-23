from typing import Protocol

from videosentimentanalysis.domain.audio import Audio
from videosentimentanalysis.domain.video import Video


class ExtractAudio(Protocol):
    def get_audio(self, video: Video) -> Audio:
        ...