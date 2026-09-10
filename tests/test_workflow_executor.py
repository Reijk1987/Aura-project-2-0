from orchestrator.agent_router.defaults import create_default_registry
from orchestrator.agent_router.router import AgentRouter
from orchestrator.planner.planner import Planner
from orchestrator.workflow_engine.executor import WorkflowExecutor


def test_executor_runs_single_step():
    registry = create_default_registry()
    router = AgentRouter(registry)
    executor = WorkflowExecutor(router)

    from orchestrator.planner.planner import PlanStep

    result = executor.execute_step(
        PlanStep("coding", "coding"),
        "Create a Python function",
    )

    assert result["agent"] == "coding"
    assert result["task"] == "Create a Python function"


def test_executor_runs_complete_plan():
    registry = create_default_registry()
    router = AgentRouter(registry)
    planner = Planner()
    executor = WorkflowExecutor(router)

    plan = planner.create_plan("coding")

    results = executor.execute_plan(
        plan,
        "Build a feature",
    )

    assert len(results) == 3
    assert results[0]["agent"] == "coding"
    assert results[1]["agent"] == "testing"
    assert results[2]["agent"] == "review"


def test_executor_handles_unknown_capability():
    registry = create_default_registry()
    router = AgentRouter(registry)
    executor = WorkflowExecutor(router)

    from orchestrator.planner.planner import PlanStep

    result = executor.execute_step(
        PlanStep("unknown", "unknown_capability"),
        "Unknown task",
    )

    assert result["status"] == "failed"
