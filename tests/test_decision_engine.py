from core.authority.models import AuthorityLevel
from core.autonomy.models import AutonomyLevel
from core.decision_engine.engine import DecisionEngine
from core.risk.models import RiskLevel


def test_allowed_decision():
    engine = DecisionEngine()

    decision = engine.evaluate(
        authority=AuthorityLevel.AUTONOMOUS,
        risk=RiskLevel.LOW,
        autonomy=AutonomyLevel.LIMITED_AUTONOMOUS,
    )

    assert decision.allowed is True


def test_denied_authority():
    engine = DecisionEngine()

    decision = engine.evaluate(
        authority=AuthorityLevel.DENIED,
        risk=RiskLevel.LOW,
        autonomy=AutonomyLevel.HIGH_AUTONOMOUS,
    )

    assert decision.allowed is False


def test_critical_risk_blocked():
    engine = DecisionEngine()

    decision = engine.evaluate(
        authority=AuthorityLevel.AUTONOMOUS,
        risk=RiskLevel.CRITICAL,
        autonomy=AutonomyLevel.HIGH_AUTONOMOUS,
    )

    assert decision.allowed is False
