import subprocess


class TerminalCapability:
    """Controlled terminal execution for AURA."""

    def run(self, command: list[str]) -> dict:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
