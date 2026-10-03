from pathlib import Path
from typing import ClassVar

from rag_pipline.ingestion.parsers.base import BaseFileParser


class TextParser(BaseFileParser):
    extensions: ClassVar[set[str]] = {".txt", ".md"}

    def extract_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8", errors="strict")
