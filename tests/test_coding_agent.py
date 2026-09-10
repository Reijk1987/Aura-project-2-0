from agents.coding.agent import CodingAgent


def test_coding_agent_capabilities():
    agent = CodingAgent()

    assert agent.can_handle("coding")
    assert agent.can_handle("python")
    assert agent.can_handle("software_development")
    assert not agent.can_handle("security")


def test_coding_agent_execute():
    agent = CodingAgent()

    result = agent.execute("Build a Python function")

    assert result["agent"] == "coding"
    assert result["task"] == "Build a Python function"
    assert result["status"] == "not_implemented"
