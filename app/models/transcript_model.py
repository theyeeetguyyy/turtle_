from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(slots=True)
class TranscriptModel:
    client_id: str
    client_name: str
    transcript: str
    agents: list[str] = field(default_factory=list)
    received_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

