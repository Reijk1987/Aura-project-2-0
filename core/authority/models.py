from enum import Enum


class AuthorityLevel(str, Enum):
    DENIED = "denied"
    APPROVAL_REQUIRED = "approval_required"
    LIMITED = "limited"
    AUTONOMOUS = "autonomous"
