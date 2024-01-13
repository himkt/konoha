from abc import ABC
from abc import abstractmethod
from typing import List

from konoha.data.token import Token


class BaseTokenizer(ABC):
    """Base class for word levelkonoha.tokenizer"""

    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def tokenize(_, text: str) -> List[Token]:
        """Abstract method forkonoha.tokenization"""
        raise NotImplementedError

    @property
    def name(self) -> str:
        """Return name ofkonoha.tokenizer"""
        return self._name
