from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


def parse_feature_for_ipadic(elem) -> Token:
    surface, feature = elem.split("\t")
    (postag, postag2, postag3, postag4, inflection, conjugation, base_form, *other) = feature.split(",")

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


def parse_feature_for_unidic(elem) -> Token:
    """
    UniDic format: https://unidic.ninjal.ac.jp/faq
    """
    surface, feaature_line = elem.split("\t")
    features = feaature_line.split(",")

    postag = features[0] or None
    postag2 = features[1] or None
    postag3 = features[2] or None
    postag4 = features[3] or None
    inflection = features[4] or None
    conjugation = features[5] or None

    if len(features) >= 10:
        yomi = features[6] or None
        base_form = features[7] or None
        pron = features[9] or None
    else:
        yomi = None
        base_form = None
        pron = None

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
    def __init__(
        self,
        user_dictionary_path: Optional[str] = None,
        system_dictionary_path: Optional[str] = None,
        dictionary_format: Optional[str] = None,
    ) -> None:
        from natto import MeCab
        super().__init__(name="mecab")
        options = []
        if isinstance(user_dictionary_path, str):
            options.append("-u {}".format(user_dictionary_path))
        if isinstance(system_dictionary_path, str):
            options.append("-d {}".format(system_dictionary_path))
        self._tokenizer = MeCab(" ".join(options))

        # If dictionary format is not specified,
        # konoha detects it by checking a name of system dictionary.
        # For instance, system_dictionary_path=mecab-ipadic-xxxx -> ipadic and
        #               system_dictionary_path=mecab-unidic-xxxx -> unidic.
        # If system_dictionary_path and dictionary_format are not given,
        # konoha assumes it uses mecab-ipadic (de facto standard).
        # Currently, konoha only supports ipadic. (TODO: unidic)
        if dictionary_format is None:
            if system_dictionary_path is None or "ipadic" in system_dictionary_path.lower():
                self._parse_feature = parse_feature_for_ipadic
            elif "unidic" in system_dictionary_path.lower():
                self._parse_feature = parse_feature_for_unidic
            else:
                raise ValueError(f"Unsupported system dictionary: {system_dictionary_path}")

        else:
            if "ipadic" == dictionary_format.lower():
                self._parse_feature = parse_feature_for_ipadic
            elif "unidic" == dictionary_format.lower():
                self._parse_feature = parse_feature_for_unidic
            else:
                raise ValueError(f"Unsupported dictionary format: {dictionary_format}")

    def tokenize(self, text: str) -> List[Token]:
        return_result = []
        parse_result = self._tokenizer.parse(text).rstrip(" ")
        for elem in parse_result.split("\n")[:-1]:
            return_result.append(self._parse_feature(elem))
        return return_result
