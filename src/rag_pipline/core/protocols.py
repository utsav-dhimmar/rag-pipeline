from pathlib import Path
from typing import Protocol

from .models import (
    Chunk,
    Document,
    RetrievedChunk,
)


class DocumentParser(Protocol):
    def parse(self, source: Path) -> Document: ...


class Chunker(Protocol):
    def chunk(self, document: Document) -> list[Chunk]: ...


class Embedder(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]: ...


class Retriever(Protocol):
    def retrieve(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[RetrievedChunk]: ...


class Reranker(Protocol):
    def rerank(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]: ...


class LLM(Protocol):
    def generate(
        self,
        prompt: str,
    ) -> str: ...
