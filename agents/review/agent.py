from agents.base import BaseAgent


class ReviewAgent(BaseAgent):
    """Specialized agent for code review tasks."""

    name = "review"

    def can_handle(self, capability: str) -> bool:
        return capability in {
            "review",
            "code_review",
            "quality_review",
        }

    def execute(self, task: str) -> dict:
        return {
            "agent": self.name,
            "task": task,
            "status": "not_implemented",
        }
