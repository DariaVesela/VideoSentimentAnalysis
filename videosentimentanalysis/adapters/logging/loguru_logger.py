from pathlib import Path

from loguru import logger

from videosentimentanalysis.usecases.protocols.logging import Logging


class LoguruLogger(Logging):

    def __init__(self, file_path: Path):
        logger.add(file_path)

    def log(self, message: str, *args, **kwargs) -> None:
        logger.info(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs) -> None:
        logger.info(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs) -> None:
        logger.error(message, *args, **kwargs)

    def debug(self, message: str, *args, **kwargs) -> None:
        logger.debug(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs) -> None:
        logger.warning(message, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs) -> None:
        logger.critical(message, *args, **kwargs)

    def exception(self, message: str, *args, **kwargs) -> None:
        logger.exception(message, *args, **kwargs)