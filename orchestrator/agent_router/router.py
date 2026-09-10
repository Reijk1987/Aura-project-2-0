from orchestrator.agent_router.models import AgentDescriptor
from orchestrator.agent_router.registry import AgentRegistry


class AgentRouter:

    def __init__(self, registry: AgentRegistry) -> None:
        self.registry = registry

    def route(self, capability: str) -> AgentDescriptor | None:
        for agent in self.registry.enabled_agents():
            if capability in agent.capabilities:
                return agent

        return None
