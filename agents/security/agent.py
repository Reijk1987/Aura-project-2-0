from agents.base import BaseAgent


class SecurityAgent(BaseAgent):
    """Specialized agent for security analysis tasks."""

    name = "security"

    def can_handle(self, capability: str) -> bool:
        return capability in {
            "security",
            "security_analysis",
            "audit",
        }

    def execute(self, task: str) -> dict:
        return {
            "agent": self.name,
            "task": task,
            "status": "not_implemented",
        }
