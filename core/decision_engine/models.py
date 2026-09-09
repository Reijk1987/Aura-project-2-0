from dataclasses import dataclass

from core.authority.models import AuthorityLevel
from core.autonomy.models import AutonomyLevel
from core.risk.models import RiskLevel


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str
    authority: AuthorityLevel
    risk: RiskLevel
    autonomy: AutonomyLevel
