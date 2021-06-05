from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class SentencepieceTokenizer(BaseTokenizer):
    def __init__(self, model_path: str) -> None:
        from sentencepiece import SentencePieceProcessor
        super().__init__(name="sentencepiece")
        self._tokenizer = SentencePieceProcessor()
        self._tokenizer.load(model_path)

    def tokenize(self, text: str) -> List[Token]:
        result = []
        for subword in self._tokenizer.EncodeAsPieces(text):
            token = Token(surface=subword)
            result.append(token)
        return result
