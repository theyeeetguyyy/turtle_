from app.services.attribute_loader import AttributeLoaderService


class DemographicsAgent:
    async def run(self, client_id: str, transcript: str) -> dict:
        return AttributeLoaderService().load(client_id, "demographics")
