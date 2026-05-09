from typing import Any, ClassVar, Dict, List

from app.utils.logger import get_logger


logger = get_logger(__name__)


class PublisherService:
    _latest_by_client: ClassVar[Dict[str, Dict[str, Any]]] = {}
    _events: ClassVar[List[Dict[str, Any]]] = []

    async def publish(self, event_name: str, payload: dict) -> None:
        event = {
            "eventName": event_name,
            "clientId": payload["clientId"],
            "payload": payload,
        }

        self.__class__._latest_by_client[payload["clientId"]] = event
        self.__class__._events.append(event)

        logger.info("event_published name=%s client_id=%s", event_name, payload["clientId"])
        print("===================================")
        print("EVENT PUBLISHED")
        print("EVENT:", event_name)
        print("PAYLOAD:", payload)
        print("===================================")

    async def get_latest_by_client(self, client_id: str) -> Dict[str, Any] | None:
        return self.__class__._latest_by_client.get(client_id)

    async def list_events(self) -> List[Dict[str, Any]]:
        return self.__class__._events

