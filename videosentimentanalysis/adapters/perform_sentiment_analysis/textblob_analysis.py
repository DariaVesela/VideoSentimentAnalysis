
from textblob import TextBlob

from videosentimentanalysis.usecases.protocols.extract_polarity_and_sensitivity import ExtractPolarityAndSensitivity


class TextBlobAnalysis(ExtractPolarityAndSensitivity):


    def get_polarity(self, text: str) -> float:
        return TextBlob(text).sentiment.polarity


    def get_sensitivity(self, text: str) -> float:
        return TextBlob(text).sentiment.polarity