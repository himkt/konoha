from tiny_tokenizer.tiny_tokenizer_token import Token
from tiny_tokenizer.word_tokenizers.tokenizer import BaseTokenizer


class KyTeaTokenizer(BaseTokenizer):
    """Wrapper class forKyTea"""

    def __init__(self, with_postag: bool = False, **kwargs):
        super(KyTeaTokenizer, self).__init__(
            name="kytea", with_postag=with_postag
        )  # NOQA
        try:
            import Mykytea
        except ModuleNotFoundError:
            raise ModuleNotFoundError("kytea is not installed")

        flag = ""
        self.kytea = Mykytea.Mykytea(flag)

    def tokenize(self, text: str):
        return_result = []

        if self.with_postag:
            response = self.kytea.getTagsToString(text)
            response = response.replace("\\ ", "<SPACE>")  # FIXME "私 は猫"
            response = response.replace("  ", " <SPACE>")

            for elem in response.split(" ")[:-1]:
                # FIXME If input contains a character "/",
                #       KyTea outputs "//補助記号/・",
                #       which breaks the simple logic elem.split("/")
                pron, postag, surface = map(
                    lambda e: e[::-1], elem[::-1].split("/", maxsplit=2))
                surface = surface.replace("<SPACE>", " ")
                return_result.append(Token(
                    surface=surface,
                    postag=postag,
                    pron=pron
                ))

        else:
            for surface in list(self.kytea.getWS(text)):
                return_result.append(Token(surface=surface))

        return return_result
