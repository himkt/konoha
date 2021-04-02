from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class WhitespaceTokenizer(BaseTokenizer):
    """Simple rule-based word tokenizer."""

    def __init__(_) -> None:
        super().__init__(name="whitespace")

    def tokenize(_, text: str) -> List[Token]:
        return [Token(surface=surface) for surface in text.split(" ")]
