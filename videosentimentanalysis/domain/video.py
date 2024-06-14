from pathlib import Path

from pydantic import BaseModel


class Video(BaseModel):
   local_storage_path : Path
   title: str

