from enum import IntEnum


class AutonomyLevel(IntEnum):
    MANUAL = 0
    ASSISTED = 1
    SUPERVISED = 2
    LIMITED_AUTONOMOUS = 3
    HIGH_AUTONOMOUS = 4
