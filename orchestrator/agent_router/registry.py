from orchestrator.agent_router.models import AgentDescriptor


class AgentRegistry:

    def __init__(self) -> None:
        self._agents: dict[str, AgentDescriptor] = {}

    def register(self, agent: AgentDescriptor) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> AgentDescriptor | None:
        return self._agents.get(name)

    def list_agents(self) -> list[AgentDescriptor]:
        return list(self._agents.values())

    def enabled_agents(self) -> list[AgentDescriptor]:
        return [
            agent
            for agent in self._agents.values()
            if agent.enabled
        ]
