from typing import List

from konoha.data.token import Token


class BaseTokenizer:
    """Base class for word levelkonoha.tokenizer"""

    def __init__(self, name: str, with_postag: bool = False, **kwargs) -> None:
        """
        Abstract class for word levelkonoha.tokenizer.

        Parameters
        ---
        name (str)
            name of akonoha.tokenizer
        with_postag (bool=False)
            flag determines ifkonoha.tokenizer include pos tags.
        **kwargs
            others.
        """
        self._name = name
        self._with_postag = with_postag

    def tokenize(self, text: str) -> List[Token]:
        """Abstract method forkonoha.tokenization"""
        raise NotImplementedError

    @property
    def name(self) -> str:
        """Return name ofkonoha.tokenizer"""
        return self._name
