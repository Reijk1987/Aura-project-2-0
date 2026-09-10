from pathlib import Path


class FileSystemCapability:
    """Controlled filesystem operations for AURA."""

    def read(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write(self, path: str, content: str) -> None:
        Path(path).write_text(content, encoding="utf-8")

    def exists(self, path: str) -> bool:
        return Path(path).exists()
