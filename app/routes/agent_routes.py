from fastapi import APIRouter

from app.controllers.agent_controller import AgentController
from app.schemas.response_schema import (
    AgentResponse,
    PublishedEventListResponse,
    PublishedEventResponse,
)
from app.schemas.transcript_schema import TranscriptRequest


router = APIRouter(tags=["extract"])


@router.post("/extract", response_model=AgentResponse)
async def extract_agents(body: TranscriptRequest):
    return await AgentController.process(body)


@router.get(
    "/extract/{client_id}",
    response_model=PublishedEventResponse,
)
async def get_extracted_result(client_id: str):
    return await AgentController.get_published_result(client_id)


@router.get(
    "/extract",
    response_model=PublishedEventListResponse,
)
async def list_extracted_events():
    return await AgentController.list_published_events()
