from tiny_tokenizer.word_tokenizers.tokenizer import BaseTokenizer
from tiny_tokenizer.token import Token


class CharacterTokenizer(BaseTokenizer):
    """Charactertiny_tokenizer.tokenizer"""

    def __init__(self):
        super(CharacterTokenizer, self).__init__("character")

    def tokenize(self, text: str):
        return [Token(surface=char) for char in list(text)]
