from typing import List

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class SudachiTokenizer(BaseTokenizer):
    def __init__(self, mode: str) -> None:
        from sudachipy import dictionary
        from sudachipy import tokenizer
        super().__init__(name="sudachi ({})".format(mode))

        try:
            self._tokenizer = dictionary.Dictionary().create()
        except KeyError:
            msg = "Loading a dictionary fails."
            msg += " ( see https://github.com/WorksApplications/SudachiPy#install-dict-packages )"  # NOQA
            raise KeyError(msg)

        _mode = mode.capitalize()
        if _mode == "A":
            self._mode = tokenizer.Tokenizer.SplitMode.A
        elif _mode == "B":
            self._mode = tokenizer.Tokenizer.SplitMode.B
        elif _mode == "C":
            self._mode = tokenizer.Tokenizer.SplitMode.C
        else:
            raise ValueError("Invalid mode is specified. Mode should be A, B, or C.")  # NOQA

    def tokenize(self, text: str) -> List[Token]:
        result = []
        for token in self._tokenizer.tokenize(text, self._mode):
            (postag, postag2, postag3, postag4, inflection, conjugation) = token.part_of_speech()
            result.append(
                Token(
                    surface=token.surface(),
                    postag=postag,
                    postag2=postag2,
                    postag3=postag3,
                    postag4=postag4,
                    inflection=inflection,
                    conjugation=conjugation,
                    base_form=token.dictionary_form(),
                    normalized_form=token.normalized_form(),
                    yomi=token.reading_form(),
                )
            )
        return result
