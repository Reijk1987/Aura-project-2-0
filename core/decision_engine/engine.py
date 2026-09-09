from core.authority.models import AuthorityLevel
from core.autonomy.models import AutonomyLevel
from core.decision_engine.models import Decision
from core.risk.models import RiskLevel


class DecisionEngine:

    def evaluate(
        self,
        authority: AuthorityLevel,
        risk: RiskLevel,
        autonomy: AutonomyLevel,
    ) -> Decision:

        if authority == AuthorityLevel.DENIED:
            return Decision(
                False,
                "Authority denied.",
                authority,
                risk,
                autonomy,
            )

        if risk == RiskLevel.CRITICAL:
            return Decision(
                False,
                "Critical-risk action requires explicit human control.",
                authority,
                risk,
                autonomy,
            )

        if authority == AuthorityLevel.APPROVAL_REQUIRED:
            return Decision(
                False,
                "Human approval required.",
                authority,
                risk,
                autonomy,
            )

        if autonomy == AutonomyLevel.MANUAL:
            return Decision(
                False,
                "Autonomy level is manual.",
                authority,
                risk,
                autonomy,
            )

        return Decision(
            True,
            "Action permitted.",
            authority,
            risk,
            autonomy,
        )
