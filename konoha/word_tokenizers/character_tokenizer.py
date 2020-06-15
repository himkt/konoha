from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class CharacterTokenizer(BaseTokenizer):
    """Characterkonoha.tokenizer"""

    def __init__(self):
        super(CharacterTokenizer, self).__init__("character")

    def tokenize(self, text: str):
        return [Token(surface=char) for char in list(text)]
