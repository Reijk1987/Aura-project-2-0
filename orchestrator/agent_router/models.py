from dataclasses import dataclass, field


@dataclass(frozen=True)
class AgentDescriptor:
    name: str
    capabilities: tuple[str, ...] = field(default_factory=tuple)
    enabled: bool = True
