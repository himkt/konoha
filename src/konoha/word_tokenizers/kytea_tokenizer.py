from typing import Any
from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


def _first_best(tag: Any, level: int) -> Optional[str]:
    # ``word.tag`` holds one list of (tag, score) candidates per tag level.
    # A level is an empty list when it is skipped (e.g. with ``-notag``).
    if level >= len(tag) or not tag[level]:
        return None
    return tag[level][0][0]


class KyTeaTokenizer(BaseTokenizer):
    def __init__(self, model_path: Optional[str] = None) -> None:
        from Mykytea import Mykytea

        super().__init__(name="kytea")

        if model_path is not None:
            self._tokenizer = Mykytea(model=model_path)
        else:
            self._tokenizer = Mykytea()

    def tokenize(self, text: str) -> List[Token]:
        tokens = []
        for word in self._tokenizer.getTags(text):
            # In the Japanese model, the first tag is the part of speech
            # and the second one is the pronunciation.
            postag = _first_best(word.tag, 0)
            pron = _first_best(word.tag, 1)
            tokens.append(Token(surface=word.surface, postag=postag, pron=pron))

        return tokens
