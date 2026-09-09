from core.authority.models import AuthorityLevel
from core.autonomy.models import AutonomyLevel
from core.decision_engine.engine import DecisionEngine
from core.risk.models import RiskLevel


class AURACore:
    """Central decision-making foundation of AURA 2.0."""

    def __init__(self) -> None:
        self.decision_engine = DecisionEngine()

    def evaluate_action(
        self,
        authority: AuthorityLevel,
        risk: RiskLevel,
        autonomy: AutonomyLevel,
    ):
        return self.decision_engine.evaluate(
            authority=authority,
            risk=risk,
            autonomy=autonomy,
        )
