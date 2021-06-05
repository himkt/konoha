from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class KyTeaTokenizer(BaseTokenizer):
    def __init__(self, model_path: Optional[str] = None) -> None:
        from Mykytea import Mykytea
        super().__init__(name="kytea")

        kytea_option = ""
        if model_path is not None:
            kytea_option += "-model {}".format(model_path)
        self._tokenizer = Mykytea(kytea_option)

    def tokenize(self, text: str) -> List[Token]:
        tokens = []
        response = self._tokenizer.getTagsToString(text)
        # FIXME Following dirty workaround is required to
        #       process inputs which include <whitespace> itself
        #       (e.g. "私 は猫")
        response = response.replace("\\ ", "<SPACE>").replace("  ", " <SPACE>")
        for elem in response.split(" ")[:-1]:
            # FIXME If input contains a character "/",
            #       KyTea outputs "//補助記号/・",
            #       which breaks the simple logic elem.split("/")
            pron, postag, surface = map(lambda e: e[::-1], elem[::-1].split("/", maxsplit=2))
            surface = surface.replace("<SPACE>", " ")
            tokens.append(Token(surface=surface, postag=postag, pron=pron))

        return tokens
