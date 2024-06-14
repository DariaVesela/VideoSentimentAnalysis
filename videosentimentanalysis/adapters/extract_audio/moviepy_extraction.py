from pathlib import Path

from videosentimentanalysis.domain.audio import Audio
from videosentimentanalysis.usecases.protocols.extract_audio import ExtractAudio
from moviepy.editor import VideoFileClip

class MoviePyAudioExtractor(ExtractAudio):

    def __init__(self, audio_output_path: Path):
        self.audio_output_path = audio_output_path
        self.audio_output_path.mkdir(parents=True, exist_ok=True)

    def get_audio(self, video) -> Audio:
        video_file = VideoFileClip(str(video.local_storage_path))
        audio_file_path = self.audio_output_path / f"{video.title}.wav"
        video_file.audio.write_audiofile(str(audio_file_path))
        return Audio(local_storage_path=audio_file_path)