from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    id: str
    content: str
    source: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Chunk:
    id: str
    document_id: str
    content: str
    chunk_index: int
    start_char: str
    end_char: str
    page: int
    token_count: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RetrievedChunk:
    chunk: Chunk
    score: float
    rank: int
    retrieval_method: str
