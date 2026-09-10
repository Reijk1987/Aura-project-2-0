from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowResult:
    """Result of an AURA workflow."""

    status: str
    steps_completed: int
    steps_failed: int

    @property
    def successful(self) -> bool:
        return self.status == "completed"
