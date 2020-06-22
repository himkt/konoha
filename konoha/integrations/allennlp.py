from typing import List
from typing import Optional

try:
    from allennlp.data.tokenizers.token import Token
    from allennlp.data.tokenizers.tokenizer import Tokenizer
except ImportError:
    from konoha.integrations._allennlp import Token
    from konoha.integrations._allennlp import Tokenizer
from overrides import overrides

from konoha.word_tokenizer import WordTokenizer


@Tokenizer.register("konoha")
class KonohaTokenizer(Tokenizer):
    """An integration for AllenNLP.
    """

    def __init__(
        self,
        tokenizer_name: str = "mecab",
        with_postag: bool = False,
        user_dictionary_path: Optional[str] = None,
        system_dictionary_path: Optional[str] = None,
        model_path: Optional[str] = None,
        mode: Optional[str] = None,
        dictionary_format: Optional[str] = None,
        start_tokens: Optional[List[str]] = None,
        end_tokens: Optional[List[str]] = None,
    ) -> None:
        self._tokenizer = WordTokenizer(
            tokenizer=tokenizer_name,
            with_postag=with_postag,
            user_dictionary_path=user_dictionary_path,
            system_dictionary_path=system_dictionary_path,
            model_path=model_path,
            mode=mode,
            dictionary_format=dictionary_format,
        )
        self._start_tokens = start_tokens or []
        self._start_tokens.reverse()
        self._end_tokens = end_tokens or []

    @overrides
    def batch_tokenize(self, texts: List[str]) -> List[List[Token]]:
        return [self.tokenize(text) for text in texts]

    @overrides
    def tokenize(self, text: str) -> List[Token]:
        konoha_tokens = self._tokenizer.tokenize(text)
        tokens = [
            Token(text=token.surface, lemma_=token.base_form, pos_=token.postag,)
            for token in konoha_tokens
        ]

        for start_token in self._start_tokens:
            tokens.insert(0, Token(start_token, 0))

        for end_token in self._end_tokens:
            tokens.append(Token(end_token, -1))

        return tokens
