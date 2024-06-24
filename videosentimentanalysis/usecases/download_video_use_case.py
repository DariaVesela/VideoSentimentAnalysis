import multiprocessing
from pathlib import Path
from threading import Thread

from videosentimentanalysis.domain.raw_video_url import RawVideoUrl
from videosentimentanalysis.domain.video import Video
from pytube import YouTube
from uuid import uuid4
from multiprocessing import Semaphore

from videosentimentanalysis.usecases.protocols.logging import Logging


class VideoUseCase:
    MAX_WORKERS = 5

    def __init__(self, video_output_directory: Path, logger: Logging):
        self.video_output_directory = video_output_directory
        # Create output directory if it does not exist
        self.video_output_directory.mkdir(parents=True, exist_ok=True)
        self.logger = logger

    @staticmethod
    def load_raw_url_video(file: Path) -> list[RawVideoUrl]:
        raw_video_urls: list[RawVideoUrl] = []
        with open(file=file, mode='r') as open_file:
            for line in open_file.readlines():
                raw_video_urls.append(RawVideoUrl(url=line))
        return raw_video_urls

    def download_video(self, raw_video_url: RawVideoUrl) -> Video:
        # Async method
        youtube_session = YouTube(url=raw_video_url.url)
        youtube_session.bypass_age_gate()
        self.logger.info(f"Bypassed age restriction for video from {raw_video_url}")
        stream = youtube_session.streams.first()
        # Adding a filename prefix so that we can store videos with the same name
        location_of_download = Path(
            stream.download(output_path=str(self.video_output_directory), filename=f"{uuid4()}.mp4"))
        self.logger.info(f"Downloaded video from {raw_video_url} saved to {location_of_download}")
        return Video(local_storage_path=location_of_download, title=youtube_session.title)

    def download_raw_videos_sequentially(self, raw_video_urls: list[RawVideoUrl]) -> list[Video]:
        sequential_videos: list[Video] = []
        for raw_video_url in raw_video_urls:
            sequential_videos.append(self.download_video(raw_video_url=raw_video_url))

        return sequential_videos

    def _download_semaphore_multiprocessing_wrapper(self, raw_video_url: RawVideoUrl,
                                                    semaphore: multiprocessing.Semaphore, results: list[Video | None],
                                                    index: int) -> None:
        with semaphore:
            self.logger.log(f"Downloading {raw_video_url} on process {index}")
            video = self.download_video(raw_video_url=raw_video_url)
            results[index] = video

    def download_raw_videos_multiprocessing(self, raw_video_urls: list[RawVideoUrl]) -> list[Video]:

        # Create a manager to share the results between processes
        manager = multiprocessing.Manager()
        results = manager.list([None] * len(raw_video_urls))

        # Create a semaphore to limit the number of workers
        semaphore = multiprocessing.Semaphore(value=self.MAX_WORKERS)
        processes = []

        for index, raw_video_url in enumerate(raw_video_urls):
            process = multiprocessing.Process(target=self._download_semaphore_multiprocessing_wrapper,
                                              args=(raw_video_url, semaphore, results, index))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return results

    def _download_semaphore_threading_wrapper(self, raw_video_url: RawVideoUrl, semaphore: Semaphore,
                                              results: list[Video | None], index: int) -> None:
        with semaphore:
            self.logger.log(f"Downloading {raw_video_url} on thread {index}")
            video = self.download_video(raw_video_url=raw_video_url)
            results[index] = video

    def download_raw_videos_threading(self, raw_video_urls: list[RawVideoUrl]):
        # Create a semaphore to limit the number of workers
        semaphore = Semaphore(value=self.MAX_WORKERS)
        # Create threads to download the videos
        threads = []
        results = [None] * len(raw_video_urls)
        for index, raw_video_url in enumerate(raw_video_urls):
            thread = Thread(target=self._download_semaphore_threading_wrapper,
                            args=(raw_video_url, semaphore, results, index))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        return results
