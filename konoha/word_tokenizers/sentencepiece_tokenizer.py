from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class SentencepieceTokenizer(BaseTokenizer):
    """Wrapper class forSentencepiece"""

    def __init__(self, model_path: str, **kwargs) -> None:
        """
        Initializer for SentencepieceTokenizer.

        Parameters
        ---
        model_path (str)
            path to sentencepiece model.
        **kwargs
            others.
        """

        try:
            import sentencepiece
        except ImportError:
            msg = "importing sentencepiece failed for some reason."
            msg += "\n  1. make sure sentencepiece is successfully installed."
            raise ImportError(msg)

        super(SentencepieceTokenizer, self).__init__("sentencepiece")
        self._tokenizer = sentencepiece.SentencePieceProcessor()
        self._tokenizer.load(model_path)

    def tokenize(self, text: str) -> List[Token]:
        result = []
        for subword in self._tokenizer.EncodeAsPieces(text):
            token = Token(surface=subword)
            result.append(token)
        return result
