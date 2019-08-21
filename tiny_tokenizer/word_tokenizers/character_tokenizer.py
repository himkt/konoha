from tiny_tokenizer.tiny_tokenizer_token import Token
from tiny_tokenizer.word_tokenizers.tokenizer import BaseTokenizer


class CharacterTokenizer(BaseTokenizer):
    """Charactertiny_tokenizer.tokenizer"""

    def __init__(self):
        super(CharacterTokenizer, self).__init__("character")

    def tokenize(self, text: str):
        return [Token(surface=char) for char in list(text)]
