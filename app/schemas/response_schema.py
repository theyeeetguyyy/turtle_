from typing import Any, Dict, List

from pydantic import BaseModel


class AgentResponse(BaseModel):
    success: bool
    clientId: str
    clientName: str
    extractedFields: Dict[str, Any]


class PublishedEventResponse(BaseModel):
    success: bool
    eventName: str
    clientId: str
    payload: Dict[str, Any]


class PublishedEventListResponse(BaseModel):
    success: bool
    count: int
    events: List[Dict[str, Any]]

