from agents.review.agent import ReviewAgent


def test_review_agent_capabilities():
    agent = ReviewAgent()

    assert agent.can_handle("review")
    assert agent.can_handle("code_review")
    assert agent.can_handle("quality_review")
    assert not agent.can_handle("security")


def test_review_agent_execute():
    agent = ReviewAgent()

    result = agent.execute("Review the latest code changes")

    assert result["agent"] == "review"
    assert result["task"] == "Review the latest code changes"
    assert result["status"] == "not_implemented"
