from fastapi import HTTPException

from app.models.transcript_model import TranscriptModel
from app.schemas.transcript_schema import TranscriptRequest
from app.services.orchestrator_service import OrchestratorService
from app.services.publisher_service import PublisherService


class AgentController:
    @staticmethod
    async def process(body: TranscriptRequest) -> dict:
        record = TranscriptModel(
            client_id=body.clientId,
            client_name=body.clientName,
            transcript=body.transcript,
            agents=body.agents,
        )

        result = await OrchestratorService().process_transcript(record)

        published_payload = {
            "clientId": body.clientId,
            "clientName": body.clientName,
            "receivedAt": record.received_at,
            "requestedAgents": body.agents,
            "result": result,
        }

        await PublisherService().publish(
            "crm.agents.completed",
            published_payload,
        )

        return {
            "success": True,
            "clientId": body.clientId,
            "clientName": body.clientName,
            "extractedFields": result,
        }

    @staticmethod
    async def get_published_result(client_id: str) -> dict:
        record = TranscriptModel(
            client_id=client_id,
            client_name=client_id,
            transcript="",
            agents=[],
        )
        result = await OrchestratorService().process_transcript(record)

        if not result:
            raise HTTPException(
                status_code=404,
                detail=f"No extracted result found for client '{client_id}'",
            )

        return {
            "success": True,
            "eventName": "crm.agents.fetch_all",
            "clientId": client_id,
            "payload": {
                "clientId": client_id,
                "result": result,
            },
        }

    @staticmethod
    async def list_published_events() -> dict:
        events = await PublisherService().list_events()
        return {
            "success": True,
            "count": len(events),
            "events": events,
        }
