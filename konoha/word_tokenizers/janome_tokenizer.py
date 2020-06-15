from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class JanomeTokenizer(BaseTokenizer):
    """Wrapper class for Janome."""

    def __init__(
        self, user_dictionary_path: Optional[str] = None, with_postag: bool = False
    ) -> None:
        try:
            from janome.tokenizer import Tokenizer
        except ImportError:
            msg = "importing janome failed for some reason."
            msg += "\n  1. make sure janome is successfully installed."
            raise ImportError(msg)

        super().__init__(name="janome", with_postag=with_postag)
        self._tokenizer = Tokenizer(udic=user_dictionary_path)

    def tokenize(self, text: str) -> List[Token]:
        return_result = []
        parse_result = self._tokenizer.tokenize(text)

        if self._with_postag:
            for morph in parse_result:
                surface = morph.surface
                postag, postag2, postag3, postag4 = morph.part_of_speech.split(",")
                inflection = morph.infl_type
                conjugation = morph.infl_form
                base_form = morph.base_form
                yomi = morph.reading
                pron = morph.phonetic

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
                    pron=pron,
                )
                return_result.append(token)

        else:
            for morph in parse_result:
                return_result.append(Token(surface=morph.surface))

        return return_result
