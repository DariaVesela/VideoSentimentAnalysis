from pathlib import Path

from videosentimentanalysis.usecases.protocols.logging import Logging
from enum import StrEnum
from datetime import datetime, UTC
class CustomLogger(Logging):

    class LogLevel(StrEnum):
        INFO = "INFO"
        ERROR = "ERROR"
        DEBUG = "DEBUG"
        WARNING = "WARNING"
        CRITICAL = "CRITICAL"
        EXCEPTION = "EXCEPTION"


    def __init__(self, file_path: Path ):
        self.file_path = file_path

    def _log(self, message: str, level: LogLevel, *args, **kwargs):
        output_message = f"{datetime.now(tz=UTC)} {level}: {message} {kwargs} {args} \n"
        with open(self.file_path, 'a+') as file:
            file.write(output_message)
        print(output_message)

    def log(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.INFO, *args, **kwargs)

    def info(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.INFO, *args, **kwargs)

    def error(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.ERROR, *args, **kwargs)

    def debug(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.DEBUG, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.WARNING, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.CRITICAL, *args, **kwargs)

    def exception(self, message: str, *args, **kwargs) -> None:
        self._log(message, self.LogLevel.EXCEPTION, *args, **kwargs)