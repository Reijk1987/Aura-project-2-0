from agents.coding.agent import CodingAgent
from agents.research.agent import ResearchAgent
from agents.review.agent import ReviewAgent
from agents.security.agent import SecurityAgent
from agents.testing.agent import TestingAgent


AGENT_CLASSES = {
    "coding": CodingAgent,
    "testing": TestingAgent,
    "review": ReviewAgent,
    "security": SecurityAgent,
    "research": ResearchAgent,
}


def create_agent(name: str):
    agent_class = AGENT_CLASSES.get(name)

    if agent_class is None:
        raise ValueError(f"Unknown agent: {name}")

    return agent_class()
