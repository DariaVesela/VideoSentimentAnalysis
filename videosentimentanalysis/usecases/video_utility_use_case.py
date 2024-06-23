from enum import StrEnum
from multiprocessing import Manager

from videosentimentanalysis.domain.audio import Audio
from videosentimentanalysis.domain.video import Video
from videosentimentanalysis.usecases.protocols.extract_audio import ExtractAudio
from videosentimentanalysis.usecases.protocols.extract_emotions import ExtractEmotions
from videosentimentanalysis.usecases.protocols.extract_polarity_and_sensitivity import ExtractPolarityAndSensitivity
from videosentimentanalysis.usecases.protocols.extract_text import ExtractText
from videosentimentanalysis.usecases.protocols.logging import Logging
from videosentimentanalysis.usecases.protocols.translate_text import LanguageOptions, TranslateText


class VideoUtilityUseCase:

    def __init__(
            self,
            video: Video,
            logger: Logging,
            extract_audio: ExtractAudio,
            extract_text: ExtractText,
            extract_polarity_and_sensitivity: ExtractPolarityAndSensitivity,
            translate: TranslateText,
            extract_emotions: ExtractEmotions
    ):
        self.video: Video = video
        self.logger: Logging = logger
        self.extract_audio_util: ExtractAudio = extract_audio
        self.extract_text_util: ExtractText = extract_text
        self._audio: Audio | None = None
        self._transcribed_audio: str | None = None
        self.extract_polarity_and_sensitivity: ExtractPolarityAndSensitivity = extract_polarity_and_sensitivity
        self.translate: TranslateText = translate
        self.extract_emotions: ExtractEmotions = extract_emotions

    def get_sentiment_analysis(self) -> tuple[float, float]:
        transcribed_audio = self.transcribe_audio()
        self.logger.info(f"Performing sentiment analysis on video {self.video.title}")
        return self.extract_polarity_and_sensitivity.get_polarity(
            transcribed_audio), self.extract_polarity_and_sensitivity.get_sensitivity(transcribed_audio)

    def extract_audio(self) -> Audio:
        if self._audio is not None:
            self.logger.info(f"Returning cached audio for video {self.video.title}")
            return self._audio
        self.logger.info(f"Extracting audio from video {self.video.title}")
        self._audio = self.extract_audio_util.get_audio(video=self.video)
        return self._audio

    def transcribe_audio(self) -> str:
        # do we already have transcribed audio?
        if self._transcribed_audio is not None:
            # if yes, then return it
            self.logger.info(f"Returning cached transcribed audio for video {self.video.title}")
            return self._transcribed_audio
        # if no, transcribe it
        extracted_audio = self.extract_audio()
        # Perform audio to text
        self.logger.log(f"Transcribing audio from video {self.video.title}")
        self._transcribed_audio = self.extract_text_util.get_text(audio=extracted_audio)
        return self._transcribed_audio

    def translate_text(self, source_lang: LanguageOptions, target_lang: LanguageOptions) -> str:
        transcribed_audio = self.transcribe_audio()
        return self.translate.translate_text(text=transcribed_audio, source_lang=source_lang, target_lang=target_lang)

    def detect_emotions(self) -> dict[str: float]:
        transcribed_audio = self.transcribe_audio()
        return self.extract_emotions.get_emotions(text=transcribed_audio)


    def _multiprocessing_wrapper_audio_extraction_wrapper(self, results, index):
        self.logger.info(f"Extracting audio using process {index}")
        results[index] = self.extract_audio()




