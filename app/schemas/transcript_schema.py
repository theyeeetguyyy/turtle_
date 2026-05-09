from typing import List

from pydantic import BaseModel, Field


class TranscriptRequest(BaseModel):
    clientId: str = Field(..., min_length=1)
    clientName: str = Field(..., min_length=1)
    transcript: str = Field(..., min_length=1)
    agents: List[str] = Field(default_factory=list)

