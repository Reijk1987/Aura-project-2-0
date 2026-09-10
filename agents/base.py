from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Base contract for every AURA agent."""

    name: str = "base"

    @abstractmethod
    def can_handle(self, capability: str) -> bool:
        """Return whether this agent can handle a capability."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, task: str) -> dict:
        """Execute a task.

        Actual execution capabilities will be added later.
        """
        raise NotImplementedError
