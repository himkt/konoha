from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class JanomeTokenizer(BaseTokenizer):
    def __init__(self, user_dictionary_path: Optional[str] = None) -> None:
        from janome.tokenizer import Tokenizer
        super().__init__(name="janome")
        self._tokenizer = Tokenizer(udic=user_dictionary_path)

    def tokenize(self, text: str) -> List[Token]:
        return_result = []
        for morph in self._tokenizer.tokenize(text):
            postag, postag2, postag3, postag4 = morph.part_of_speech.split(",")
            token = Token(
                surface=morph.surface,
                postag=postag,
                postag2=postag2,
                postag3=postag3,
                postag4=postag4,
                inflection=morph.infl_type,
                conjugation=morph.infl_form,
                base_form=morph.base_form,
                yomi=morph.reading,
                pron=morph.phonetic,
            )
            return_result.append(token)

        return return_result
