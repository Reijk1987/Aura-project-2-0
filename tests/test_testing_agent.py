from agents.testing.agent import TestingAgent


def test_testing_agent_capabilities():
    agent = TestingAgent()

    assert agent.can_handle("testing")
    assert agent.can_handle("pytest")
    assert agent.can_handle("test_execution")
    assert not agent.can_handle("coding")


def test_testing_agent_execute():
    agent = TestingAgent()

    result = agent.execute("Run the project tests")

    assert result["agent"] == "testing"
    assert result["task"] == "Run the project tests"
    assert result["status"] == "not_implemented"
