from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class NagisaTokenizer(BaseTokenizer):
    def __init__(self) -> None:
        from nagisa import Tagger
        super().__init__(name="nagisa")
        self._tokenizer = Tagger()

    def tokenize(self, text: str) -> List[Token]:
        response = self._tokenizer.tagging(text)
        tokens = [
            Token(surface=surface, postag=postag) for (surface, postag) in zip(response.words, response.postags)
        ]
        return tokens
