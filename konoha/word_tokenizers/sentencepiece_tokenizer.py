from konoha.konoha_token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class SentencepieceTokenizer(BaseTokenizer):
    """Wrapper class forSentencepiece"""

    def __init__(self, model_path: str, **kwargs):
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
        self.tokenizer = sentencepiece.SentencePieceProcessor()
        self.tokenizer.load(model_path)

    def tokenize(self, text: str):
        result = []
        for subword in self.tokenizer.EncodeAsPieces(text):
            token = Token(surface=subword)
            result.append(token)
        return result
