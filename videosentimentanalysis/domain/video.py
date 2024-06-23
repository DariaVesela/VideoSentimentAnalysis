from pathlib import Path

from pydantic import BaseModel


class Video(BaseModel):
    local_storage_path: Path
    title: str

    def move(self, new_path: Path) -> Path:
        self.local_storage_path = self.local_storage_path.rename(new_path / self.local_storage_path.name)
        return self.local_storage_path
