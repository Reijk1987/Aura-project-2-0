from dataclasses import dataclass


@dataclass(frozen=True)
class PlanStep:
    name: str
    capability: str


class Planner:
    """Creates a simple execution plan."""

    def create_plan(self, capability: str) -> list[PlanStep]:
        return [
            PlanStep("execute", capability),
            PlanStep("test", "testing"),
            PlanStep("review", "review"),
        ]
