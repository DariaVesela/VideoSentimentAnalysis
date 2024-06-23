from videosentimentanalysis.domain.audio import Audio
from videosentimentanalysis.usecases.protocols.extract_text import ExtractText
import speech_recognition as sr

class SpeechRecognition(ExtractText):

    def get_text(self, audio: Audio) -> str:
        recognizer = sr.Recognizer()
        with audio.local_storage_path.open("rb") as audio_file:
            with sr.AudioFile(audio_file) as source:
                audio_data = recognizer.record(source)
                return recognizer.recognize_whisper(audio_data)
