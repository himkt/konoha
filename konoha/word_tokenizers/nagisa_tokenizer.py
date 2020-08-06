from typing import List
from typing import Optional

from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class NagisaTokenizer(BaseTokenizer):
    """Wrapper class for Nagisa"""

    def __init__(
        self, with_postag: bool = False, **kwargs
    ) -> None:

        super(NagisaTokenizer, self).__init__(
            name="nagisa", with_postag=with_postag
        )
        try:
            import nagisa
            self._tokenizer = nagisa
        except ImportError:
            msg = "Importing nagisa failed for some reason."
            msg += "\n  1. make sure nagisa is successfully installed."
            raise ImportError(msg)

    def tokenize(self, text: str) -> List[Token]:
        response = self._tokenizer.tagging(text)

        if self._with_postag:
            tokens = [Token(surface=surface, postag=postag) for (surface, postag) in zip(response.words, response.postags)]
        else:
            tokens = [Token(surface=surface) for surface in response.words]

        return tokens
