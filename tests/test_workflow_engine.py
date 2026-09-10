from orchestrator.agent_router.defaults import create_default_registry
from orchestrator.agent_router.router import AgentRouter
from orchestrator.planner.planner import Planner
from orchestrator.workflow_engine.engine import WorkflowEngine


def test_planner_creates_execution_plan():
    planner = Planner()

    plan = planner.create_plan("coding")

    assert len(plan) == 3
    assert plan[0].capability == "coding"
    assert plan[1].capability == "testing"
    assert plan[2].capability == "review"


def test_workflow_resolves_agents():
    registry = create_default_registry()
    router = AgentRouter(registry)
    planner = Planner()
    workflow = WorkflowEngine(router)

    plan = planner.create_plan("coding")
    agents = workflow.resolve_plan(plan)

    assert agents[0].name == "coding"
    assert agents[1].name == "testing"
    assert agents[2].name == "review"


def test_security_agent_can_be_resolved():
    registry = create_default_registry()
    router = AgentRouter(registry)
    workflow = WorkflowEngine(router)

    from orchestrator.planner.planner import PlanStep

    agent = workflow.resolve_step(
        PlanStep("security_check", "security")
    )

    assert agent.name == "security"
