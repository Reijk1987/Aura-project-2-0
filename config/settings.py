"""AURA 2.0 configuration."""

PROJECT_NAME = "AURA 2.0"
VERSION = "0.1.0"

ENVIRONMENT = "development"

# Safety defaults
AUTONOMY_ENABLED = False
EXECUTION_ENABLED = False
NETWORK_ACCESS_ENABLED = False

# Every action must pass through authorization and risk checks.
REQUIRE_AUTHORIZATION = True
REQUIRE_VERIFICATION = True
REQUIRE_AUDIT = True
