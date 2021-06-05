from typing import List

import nagisa

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class NagisaTokenizer(BaseTokenizer):
    def __init__(self) -> None:
        super().__init__(name="nagisa")
        self._tokenizer = nagisa

    def tokenize(self, text: str) -> List[Token]:
        response = self._tokenizer.tagging(text)
        tokens = [
            Token(surface=surface, postag=postag) for (surface, postag) in zip(response.words, response.postags)
        ]
        return tokens
