from typing import Optional
from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


def parse_feature_for_ipadic(elem) -> Token:
    surface, feature = elem.split("\t")
    (
        postag,
        postag2,
        postag3,
        postag4,
        inflection,
        conjugation,
        base_form,
        *other,
    ) = feature.split(",")

    # For words not in a dictionary
    if len(other) == 2:
        yomi, pron = other
    else:
        yomi, pron = None, None

    return Token(
        surface=surface,
        postag=postag,
        postag2=postag2,
        postag3=postag3,
        postag4=postag4,
        inflection=inflection,
        conjugation=conjugation,
        base_form=base_form,
        yomi=yomi,
        pron=pron,
    )


class MeCabTokenizer(BaseTokenizer):
    """Wrapper class forexternal text analyzers"""

    def __init__(
        self,
        user_dictionary_path: Optional[str] = None,
        system_dictionary_path: Optional[str] = None,
        dictionary_format: Optional[str] = None,
        with_postag: bool = False,
    ) -> None:
        """
        Initializer for MeCabTokenizer.

        Parameters
        ---
        dictionary_path (Optional[str]=None)
            path to a custom dictionary (option)
            it is used by `mecab -u [dictionary_path]`
        with_postag (bool=False)
            flag determines ifkonoha.tokenizer include pos tags.
        """
        try:
            import natto
        except ImportError:
            msg = "importing natto-py failed for some reason."
            msg += "\n  1. make sure MeCab is successfully installed."
            msg += "\n  2. make sure natto-py is successfully installed."
            raise ImportError(msg)

        super().__init__(name="mecab", with_postag=with_postag)

        flag = ""

        if not self._with_postag:
            flag += " -Owakati"

        if isinstance(user_dictionary_path, str):
            flag += " -u {}".format(user_dictionary_path)

        if isinstance(system_dictionary_path, str):
            flag += " -d {}".format(system_dictionary_path)

        self._tokenizer = natto.MeCab(flag)

        # If dictionary format is not specified,
        # konoha detects it by checking a name of system dictionary.
        # For instance, system_dictionary_path=mecab-ipadic-xxxx -> ipadic and
        #               system_dictionary_path=mecab-unidic-xxxx -> unidic.
        # If system_dictionary_path and dictionary_format are not given,
        # konoha assumes it uses mecab-ipadic (de facto standard).
        # Currently, konoha only supports ipadic. (TODO: unidic)
        if dictionary_format is None:
            if system_dictionary_path is None or system_dictionary_path.lower() in "ipadic":
                self._parse_feature = parse_feature_for_ipadic
            else:
                raise ValueError(f"Unsupported system dictionary: {system_dictionary_path}")

        else:
            if "ipadic" == dictionary_format.lower():
                self._parse_feature = parse_feature_for_ipadic
            else:
                raise ValueError(f"Unsupported dictionary format: {dictionary_format}")

    def tokenize(self, text: str) -> List[Token]:
        """Tokenize"""
        return_result = []
        parse_result = self._tokenizer.parse(text).rstrip(" ")
        if self._with_postag:
            for elem in parse_result.split("\n")[:-1]:
                return_result.append(self._parse_feature(elem))
        else:
            for surface in parse_result.split(" "):
                return_result.append(Token(surface=surface))

        return return_result
