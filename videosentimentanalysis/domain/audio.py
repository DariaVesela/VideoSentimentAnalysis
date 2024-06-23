from pathlib import Path

from pydantic import BaseModel


class Audio(BaseModel):
    local_storage_path : Path

    def move(self, new_path: Path) -> Path:
        self.local_storage_path = self.local_storage_path.rename(new_path / self.local_storage_path.name)
        return self.local_storage_path
