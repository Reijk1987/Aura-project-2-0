from agents.security.agent import SecurityAgent


def test_security_agent_capabilities():
    agent = SecurityAgent()

    assert agent.can_handle("security")
    assert agent.can_handle("security_analysis")
    assert agent.can_handle("audit")
    assert not agent.can_handle("coding")


def test_security_agent_execute():
    agent = SecurityAgent()

    result = agent.execute("Scan the project for security issues")

    assert result["agent"] == "security"
    assert result["task"] == "Scan the project for security issues"
    assert result["status"] == "not_implemented"
