from orchestrator.agent_router.agent_map import create_agent
from orchestrator.agent_router.router import AgentRouter
from orchestrator.planner.planner import PlanStep


class WorkflowExecutor:
    """Executes workflow steps using the routed agents."""

    def __init__(self, router: AgentRouter) -> None:
        self.router = router

    def execute_step(self, step: PlanStep, task: str) -> dict:
        descriptor = self.router.route(step.capability)

        if descriptor is None:
            return {
                "status": "failed",
                "reason": f"No agent available for capability: {step.capability}",
            }

        agent = create_agent(descriptor.name)

        return agent.execute(task)

    def execute_plan(
        self,
        steps: list[PlanStep],
        task: str,
    ) -> list[dict]:
        results = []

        for step in steps:
            results.append(
                self.execute_step(
                    step=step,
                    task=task,
                )
            )

        return results
