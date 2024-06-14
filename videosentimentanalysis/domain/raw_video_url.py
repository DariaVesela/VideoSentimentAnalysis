from pydantic import BaseModel
class RawVideoUrl(BaseModel):
    url: str
