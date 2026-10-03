from abc import ABC, abstractmethod
from pathlib import Path
from typing import ClassVar
from uuid import uuid7

from rag_pipline.core.exceptions import NotSupported
from rag_pipline.core.models import Document


class BaseFileParser(ABC):
    extensions: ClassVar[set[str]] = set()

    def parse(self, path: Path) -> Document:
        self.validate(path)
        text = self.extract_text(path)  # implemented per-type with lib
        return Document(id=str(uuid7()), content=text, source=str(path))

    def validate(self, path: Path):
        if not path.is_file():
            raise FileNotFoundError(f"{path} does not exists")

        if path.suffix not in self.extensions:
            raise NotSupported(
                f"{path.suffix} is not supported by {type(self).__name__}"
            )

    @abstractmethod
    def extract_text(self, path: Path) -> str: ...
