from orchestrator.agent_router.models import AgentDescriptor
from orchestrator.agent_router.registry import AgentRegistry


def create_default_registry() -> AgentRegistry:
    registry = AgentRegistry()

    registry.register(
        AgentDescriptor(
            name="coding",
            capabilities=("coding", "python", "software_development"),
        )
    )

    registry.register(
        AgentDescriptor(
            name="testing",
            capabilities=("testing", "pytest", "test_execution"),
        )
    )

    registry.register(
        AgentDescriptor(
            name="review",
            capabilities=("review", "code_review", "quality_review"),
        )
    )

    registry.register(
        AgentDescriptor(
            name="security",
            capabilities=("security", "security_analysis", "audit"),
        )
    )

    registry.register(
        AgentDescriptor(
            name="research",
            capabilities=("research", "information_gathering", "analysis"),
        )
    )

    return registry
