from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class KyTeaTokenizer(BaseTokenizer):
    """Wrapper class forKyTea"""

    def __init__(
        self, with_postag: bool = False, model_path: Optional[str] = None, **kwargs
    ) -> None:

        super(KyTeaTokenizer, self).__init__(
            name="kytea", with_postag=with_postag, model_path=model_path
        )
        try:
            import Mykytea
        except ImportError:
            msg = "importing kytea failed for some reason."
            msg += "\n  1. make sure KyTea is successfully installed."
            msg += "\n  2. make sure Mykytea-python is successfully installed."
            raise ImportError(msg)

        kytea_option = ""
        if model_path is not None:
            kytea_option += "-model {}".format(model_path)
        self._tokenizer = Mykytea.Mykytea(kytea_option)

    def tokenize(self, text: str) -> List[Token]:
        tokens = []

        if self._with_postag:
            response = self._tokenizer.getTagsToString(text)

            # FIXME Following dirty workaround is required to
            #       process inputs which include <whitespace> itself
            #       (e.g. "私 は猫")
            response = response.replace("\\ ", "<SPACE>").replace("  ", " <SPACE>")

            for elem in response.split(" ")[:-1]:
                # FIXME If input contains a character "/",
                #       KyTea outputs "//補助記号/・",
                #       which breaks the simple logic elem.split("/")
                pron, postag, surface = map(
                    lambda e: e[::-1], elem[::-1].split("/", maxsplit=2)
                )
                surface = surface.replace("<SPACE>", " ")
                tokens.append(Token(surface=surface, postag=postag, pron=pron))

        else:
            for surface in list(self._tokenizer.getWS(text)):
                tokens.append(Token(surface=surface))

        return tokens
