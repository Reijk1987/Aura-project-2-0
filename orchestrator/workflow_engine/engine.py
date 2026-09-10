from orchestrator.agent_router.router import AgentRouter
from orchestrator.planner.planner import PlanStep


class WorkflowEngine:
    """Coordinates planned steps with available agents."""

    def __init__(self, router: AgentRouter) -> None:
        self.router = router

    def resolve_step(self, step: PlanStep):
        return self.router.route(step.capability)

    def resolve_plan(self, steps: list[PlanStep]):
        return [
            self.resolve_step(step)
            for step in steps
        ]
