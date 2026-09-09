from core.authority.models import AuthorityLevel
from core.autonomy.models import AutonomyLevel
from core.risk.models import RiskLevel
from core.system import AURACore


def test_core_allows_safe_action():
    core = AURACore()

    decision = core.evaluate_action(
        authority=AuthorityLevel.AUTONOMOUS,
        risk=RiskLevel.LOW,
        autonomy=AutonomyLevel.LIMITED_AUTONOMOUS,
    )

    assert decision.allowed is True


def test_core_blocks_critical_action():
    core = AURACore()

    decision = core.evaluate_action(
        authority=AuthorityLevel.AUTONOMOUS,
        risk=RiskLevel.CRITICAL,
        autonomy=AutonomyLevel.HIGH_AUTONOMOUS,
    )

    assert decision.allowed is False
