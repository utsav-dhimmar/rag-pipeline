# Project Structure

thanks chatGPT

```sh
rag-project/
│
├── pyproject.toml
├── uv.lock
├── README.md
├── .env
├── .env.example
├── .gitignore
│
├── src/
│   └── rag/
│       │
│       ├── __init__.py
│       ├── config.py
│       │
│       ├── core/
│       │   ├── models.py
│       │   ├── protocols.py
│       │   └── exceptions.py
│       │
│       ├── ingestion/
│       │   ├── pipeline.py
│       │   ├── parsers/
│       │   │   ├── base.py
│       │   │   ├── pdf.py
│       │   │   ├── docx.py
│       │   │   └── ...
│       │   │
│       │   └── normalizer.py
│       │
│       ├── chunking/
│       │   ├── base.py
│       │   ├── recursive.py
│       │   ├── semantic.py
│       │   └── structure.py
│       │
│       ├── embeddings/
│       │   ├── base.py
│       │   └── providers/
│       │       ├── ollama.py
│       │       ├── openai.py
│       │       └── ...
│       │
│       ├── storage/
│       │   ├── base.py
│       │   ├── postgres.py
│       │   ├── documents.py
│       │   └── chunks.py
│       │
│       ├── retrieval/
│       │   ├── base.py
│       │   ├── dense.py
│       │   ├── sparse.py
│       │   ├── hybrid.py
│       │   └── rrf.py
│       │
│       ├── reranking/
│       │   ├── base.py
│       │   └── cross_encoder.py
│       │
│       ├── generation/
│       │   ├── base.py
│       │   ├── llm.py
│       │   ├── prompts.py
│       │   └── context.py
│       │
│       ├── evaluation/
│       │   ├── datasets.py
│       │   ├── retrieval.py
│       │   └── generation.py
│       │
│       └── observability/
│           ├── tracing.py
│           └── phoenix.py
│
├── tests/
│   │
│   ├── unit/
│   │   ├── chunking/
│   │   ├── retrieval/
│   │   ├── reranking/
│   │   └── ...
│   │
│   ├── integration/
│   │   ├── ingestion/
│   │   ├── storage/
│   │   └── retrieval/
│   │
│   └── fixtures/
│
├── scripts/
│   ├── ingest.py
│   └── evaluate.py
│
└── data/
    ├── raw/
    ├── processed/
    └── evaluation/
```
