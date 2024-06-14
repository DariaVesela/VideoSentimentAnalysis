from typing import Protocol

class Logging(Protocol):
    def log(self, message: str, *args, **kwargs) -> None:
        ...

    def info(self, message: str, *args, **kwargs) -> None:
        ...

    def error(self, message: str, *args, **kwargs) -> None:
        ...

    def debug(self, message: str, *args, **kwargs) -> None:
        ...

    def warning(self, message: str, *args, **kwargs) -> None:
        ...

    def critical(self, message: str, *args, **kwargs) -> None:
        ...

    def exception(self, message: str, *args, **kwargs) -> None:
        ...


