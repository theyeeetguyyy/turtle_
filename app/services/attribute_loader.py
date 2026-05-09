import json
from pathlib import Path
from typing import Any


class AttributeLoaderService:
    def __init__(self) -> None:
        self.base_path = Path("output attributes")

    def load(self, client_id: str, agent_slug: str) -> dict[str, Any]:
        organized_path = self.base_path / client_id / f"{agent_slug}.json"
        legacy_path = self.base_path / f"{client_id}_{agent_slug}.json"

        file_path = organized_path if organized_path.exists() else legacy_path
        if not file_path.exists():
            return {
                "client_id": client_id,
                "agent": agent_slug,
                "status": "missing_output_file",
                "message": f"No demo output file found at '{file_path.as_posix()}'",
            }

        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
