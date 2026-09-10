from orchestrator.agent_router.models import AgentDescriptor
from orchestrator.agent_router.registry import AgentRegistry
from orchestrator.agent_router.router import AgentRouter


def test_agent_registry():
    registry = AgentRegistry()

    coding_agent = AgentDescriptor(
        name="coding",
        capabilities=("coding", "python"),
    )

    registry.register(coding_agent)

    assert registry.get("coding") == coding_agent
    assert len(registry.list_agents()) == 1


def test_agent_router():
    registry = AgentRegistry()

    registry.register(
        AgentDescriptor(
            name="coding",
            capabilities=("coding", "python"),
        )
    )

    registry.register(
        AgentDescriptor(
            name="security",
            capabilities=("security", "audit"),
        )
    )

    router = AgentRouter(registry)

    result = router.route("coding")

    assert result is not None
    assert result.name == "coding"


def test_router_returns_none_for_unknown_capability():
    registry = AgentRegistry()

    registry.register(
        AgentDescriptor(
            name="coding",
            capabilities=("coding",),
        )
    )

    router = AgentRouter(registry)

    assert router.route("security") is None
