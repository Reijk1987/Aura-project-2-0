from capabilities.filesystem.service import FileSystemCapability
from capabilities.terminal.service import TerminalCapability


def test_filesystem_write_read_and_exists(tmp_path):
    filesystem = FileSystemCapability()

    path = tmp_path / "test.txt"

    filesystem.write(str(path), "AURA")

    assert filesystem.exists(str(path))
    assert filesystem.read(str(path)) == "AURA"


def test_terminal_runs_command():
    terminal = TerminalCapability()

    result = terminal.run(
        ["python", "-c", "print('AURA')"]
    )

    assert result["returncode"] == 0
    assert "AURA" in result["stdout"]
