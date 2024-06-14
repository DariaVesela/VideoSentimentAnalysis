from pathlib import Path

from pydantic import BaseModel


class Audio(BaseModel):
    local_storage_path : Path
