from agents.base import BaseAgent


class TestingAgent(BaseAgent):
    """Specialized agent for software testing tasks."""

    name = "testing"

    def can_handle(self, capability: str) -> bool:
        return capability in {
            "testing",
            "pytest",
            "test_execution",
        }

    def execute(self, task: str) -> dict:
        return {
            "agent": self.name,
            "task": task,
            "status": "not_implemented",
        }
