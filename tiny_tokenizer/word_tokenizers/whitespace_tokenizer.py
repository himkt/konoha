from tiny_tokenizer.tiny_tokenizer_token import Token
from tiny_tokenizer.word_tokenizers.tokenizer import BaseTokenizer


class WhitespaceTokenizer(BaseTokenizer):
    """Whitespace_tokenizer.tokenizer"""

    def __init__(self):
        super(WhitespaceTokenizer, self).__init__("whitespace")

    def tokenize(self, text: str):
        return [Token(surface=surface) for surface in text.split(" ")]
