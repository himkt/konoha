from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class CharacterTokenizer(BaseTokenizer):
    def __init__(self):
        super().__init__(name="character")

    def tokenize(_, text: str):
        return [Token(surface=char) for char in list(text)]
