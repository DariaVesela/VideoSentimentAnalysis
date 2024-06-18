import text2emotion as te
from videosentimentanalysis.usecases.protocols.extract_emotions import ExtractEmotions

class GetEmotions(ExtractEmotions):
    def get_emotions(self, text:str) -> dict[str,int]:
        emotions = te.get_emotion(text)
        return emotions


