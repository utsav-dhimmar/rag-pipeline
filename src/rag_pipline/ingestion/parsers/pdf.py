from pathlib import Path
from typing import ClassVar
from uuid import uuid7

from pymupdf import Document as PymupdfDocument
from pymupdf import open as pymupdf_open

from rag_pipline.core.models import Document
from rag_pipline.ingestion.parsers.base import BaseFileParser


class PDFParser(BaseFileParser):
    extensions: ClassVar[set[str]] = {".pdf"}

    def extract_text(self, path: Path) -> str:
        pages: list[str] = []
        with pymupdf_open(filename=path) as doc:  # type: pymupdf.Document
            doc: PymupdfDocument
            for i, page in enumerate(iterable=doc, start=1):
                text: str = page.get_text("text") or ""
                pages.append(f"\n\n[PAGE {i}]\n\n{text.strip()}")

        return "".join(pages).strip()

    def parse(self, path: Path) -> Document:
        self.validate(path)

        with pymupdf_open(filename=path) as doc:
            doc: PymupdfDocument
            page_count = doc.page_count

        text = self.extract_text(path)
        return Document(
            id=str(uuid7()),
            source=str(path),
            content=text,
            metadata={"page_count": page_count, "parser": "pymupdf"},
        )
