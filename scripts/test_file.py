from pathlib import Path


def read_text():
    from rag_pipline.ingestion.parsers.text import TextParser

    doc = TextParser().parse(path=Path("./data/raw/make.md").resolve())

    print(doc)


def read_pdf():
    from rag_pipline.ingestion.parsers.pdf import PDFParser

    doc = PDFParser().parse(path=Path("./data/raw/syllabus.pdf").resolve())
    print(doc)


def main() -> None:
    read_text()


if __name__ == "__main__":
    main()
