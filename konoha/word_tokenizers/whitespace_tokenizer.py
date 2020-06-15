from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class WhitespaceTokenizer(BaseTokenizer):
    """Whitespace_tokenizer.tokenizer"""

    def __init__(self) -> None:
        super(WhitespaceTokenizer, self).__init__("whitespace")

    def tokenize(self, text: str) -> List[Token]:
        return [Token(surface=surface) for surface in text.split(" ")]
