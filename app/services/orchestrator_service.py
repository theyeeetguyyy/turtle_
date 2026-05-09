from app.models.transcript_model import TranscriptModel
from app.services.agents.demographics_agent import DemographicsAgent
from app.services.agents.feedback_agent import FeedbackAgent
from app.services.agents.finance_agent import FinanceAgent
from app.services.agents.goals_agent import GoalsAgent
from app.services.agents.professional_agent import ProfessionalAgent
from app.services.agents.qualitative_agent import QualitativeAgent
from app.services.agents.schedule_agent import ScheduleAgent
from app.services.agents.system_resolver import SystemResolver
from app.services.agents.task_agent import TaskAgent


class OrchestratorService:
    def __init__(self) -> None:
        self.agent_registry = {
            "DemographicsAgent": ("demographics", DemographicsAgent),
            "FinanceAgent": ("finance", FinanceAgent),
            "GoalsAgent": ("goals", GoalsAgent),
            "ProfessionalAgent": ("professional", ProfessionalAgent),
            "QualitativeAgent": ("qualitative", QualitativeAgent),
            "ScheduleAgent": ("schedule", ScheduleAgent),
            "TaskAgent": ("tasks", TaskAgent),
            "FeedbackAgent": ("feedback", FeedbackAgent),
            "SystemResolver": ("system", SystemResolver),
        }

    async def process_transcript(self, record: TranscriptModel) -> dict:
        requested_agents = record.agents or list(self.agent_registry.keys())
        final_output: dict[str, dict] = {}

        for agent_name in requested_agents:
            agent_config = self.agent_registry.get(agent_name)
            if not agent_config:
                final_output[agent_name] = {
                    "error": f"Unknown agent '{agent_name}'",
                }
                continue

            response_key, agent_class = agent_config
            final_output[response_key] = await agent_class().run(
                record.client_id,
                record.transcript,
            )

        return final_output
