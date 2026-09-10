from agents.base import BaseAgent


class ResearchAgent(BaseAgent):
    """Specialized agent for research tasks."""

    name = "research"

    def can_handle(self, capability: str) -> bool:
        return capability in {
            "research",
            "information_gathering",
            "analysis",
        }

    def execute(self, task: str) -> dict:
        return {
            "agent": self.name,
            "task": task,
            "status": "not_implemented",
        }
