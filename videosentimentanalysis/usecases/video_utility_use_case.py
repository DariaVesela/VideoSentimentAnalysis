from enum import StrEnum

from videosentimentanalysis.domain.audio import Audio
from videosentimentanalysis.domain.video import Video
from videosentimentanalysis.usecases.protocols.extract_audio import ExtractAudio
from videosentimentanalysis.usecases.protocols.extract_text import ExtractText
from videosentimentanalysis.usecases.protocols.logging import Logging


class LanguageOptions(StrEnum):
    ENGLISH = "EN"
    SPANISH = "ES"

class VideoUtilityUseCase:

    def __init__(self, video: Video, logger: Logging, extract_audio: ExtractAudio, extract_text: ExtractText):
        self.video: Video = video
        self.logger: Logging = logger
        self.extract_audio_util: ExtractAudio = extract_audio
        self.extract_text_util: ExtractText = extract_text
        self._audio: Audio|None = None

    def get_sentiment_analysis(self) -> tuple[float, float]:
        transcribed_audio = self.transcribe_audio()
        # Perform analsis

    def extract_audio(self) -> Audio:
        if self._audio is not None:
            self.logger.info(f"Returning cached audio for video {self.video.title}")
            return self._audio
        self.logger.info(f"Extracting audio from video {self.video.title}")
        self._audio = self.extract_audio_util.get_audio(video=self.video)
        return self._audio


    def transcribe_audio(self) -> str:
        extracted_audio = self.extract_audio()
        # Perform audio to text
        self.logger.log(f"Transcribing audio from video {self.video.title}")
        return self.extract_text_util.get_text(audio=extracted_audio)

    def translate_text(self, source_lang:LanguageOptions, target_lang:LanguageOptions) -> str:
        transcribed_audio = self.transcribe_audio()

    def detect_emotions(self) -> dict[str: float]:
        transcribed_audio = self.transcribe_audio()

