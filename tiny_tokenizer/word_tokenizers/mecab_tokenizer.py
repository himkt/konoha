from typing import Optional

from tiny_tokenizer.tiny_tokenizer_token import Token
from tiny_tokenizer.word_tokenizers.tokenizer import BaseTokenizer


class MeCabTokenizer(BaseTokenizer):
    """Wrapper class forexternal text analyzers"""

    def __init__(
        self, dictionary_path: Optional[str] = None, with_postag: bool = False
    ):
        """
        Initializer for MeCabTokenizer.

        Parameters
        ---
        dictionary_path (Optional[str]=None)
            path to a custom dictionary (option)
            it is used by `mecab -u [dictionary_path]`
        with_postag (bool=False)
            flag determines iftiny_tokenizer.tokenizer include pos tags.
        """
        super().__init__(
            name="mecab",
            with_postag=with_postag)

        try:
            import natto
        except ImportError:
            raise ImportError("natto-py is not installed")

        flag = ""
        if not self.with_postag:
            flag += " -Owakati"

        if dictionary_path is not None:
            flag += " -u {}".format(dictionary_path)

        self.mecab = natto.MeCab(flag)

    def tokenize(self, text: str):
        """Tokenize"""
        return_result = []
        parse_result = self.mecab.parse(text)
        if self.with_postag:
            for elem in parse_result.split("\n")[:-1]:
                surface, feature = elem.split()
                postag, postag2, postag3, postag4, \
                    inflection, conjugation, \
                    base_form, *other = feature.split(",")

                # For words not in a dictionary
                if len(other) == 2:
                    yomi, pron = other
                else:
                    yomi, pron = None, None

                token = Token(
                    surface=surface,
                    postag=postag,
                    postag2=postag2,
                    postag3=postag3,
                    postag4=postag4,
                    inflection=inflection,
                    conjugation=conjugation,
                    base_form=base_form,
                    yomi=yomi,
                    pron=pron)
                return_result.append(token)
        else:
            for surface in parse_result.split(" "):
                return_result.append(Token(surface=surface))

        return return_result
