from tiny_tokenizer.tiny_tokenizer_token import Token
from tiny_tokenizer.word_tokenizers.tokenizer import BaseTokenizer


class KyTeaTokenizer(BaseTokenizer):
    """Wrapper class forKyTea"""

    def __init__(self, with_postag: bool = False, **kwargs):
        super(KyTeaTokenizer, self).__init__(
            name="kytea",
            with_postag=with_postag)
        try:
            import Mykytea
        except ImportError:
            raise ImportError("kytea is not installed")

        self.kytea = Mykytea.Mykytea("")

    def tokenize(self, text: str):
        tokens = []

        if self.with_postag:
            response = self.kytea.getTagsToString(text)

            # FIXME Following dirty workaround is required to
            #       process inputs which include <whitespace> itself
            #       (e.g. "私 は猫")
            response = response \
                .replace("\\ ", "<SPACE>") \
                .replace("  ", " <SPACE>")

            for elem in response.split(" ")[:-1]:
                # FIXME If input contains a character "/",
                #       KyTea outputs "//補助記号/・",
                #       which breaks the simple logic elem.split("/")
                pron, postag, surface = map(
                    lambda e: e[::-1], elem[::-1].split("/", maxsplit=2))
                surface = surface.replace("<SPACE>", " ")
                tokens.append(Token(
                    surface=surface,
                    postag=postag,
                    pron=pron
                ))

        else:
            for surface in list(self.kytea.getWS(text)):
                tokens.append(Token(surface=surface))

        return tokens
