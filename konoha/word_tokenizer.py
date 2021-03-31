"""Word Level Tokenizer."""
import warnings
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import requests

from konoha import word_tokenizers
from konoha.data.resource import Resource
from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class WordTokenizer:
    """Tokenizer takes a sentence into tokens."""

    def __init__(
        self,
        tokenizer: str = "MeCab",
        with_postag: bool = False,
        user_dictionary_path: Optional[str] = None,
        system_dictionary_path: Optional[str] = None,
        model_path: Optional[str] = None,
        mode: Optional[str] = None,
        dictionary_format: Optional[str] = None,
        endpoint: Optional[str] = None,
    ) -> None:
        """Create tokenizer.

        Keyword Arguments:
            tokenizer {str or None} -- specify the type of tokenizer (default: {None})  # NOQA
            flags {str} -- option passing to tokenizer (default: {''})
        """
        user_dictionary = Resource(user_dictionary_path)
        system_dictionary = Resource(system_dictionary_path)
        model = Resource(model_path)

        self._tokenizer_name = tokenizer.lower()
        self._with_postag = with_postag
        self._user_dictionary_path = user_dictionary.path
        self._system_dictionary_path = system_dictionary.path
        self._model_path = model.path
        self._mode = mode.lower() if mode is not None else None
        self._dictionary_format = dictionary_format
        self._tokenizer = None  # type: Any
        self._endpoint = endpoint

        if not isinstance(endpoint, str):
            self._setup_tokenizer()

    def _setup_tokenizer(self) -> None:
        if self._tokenizer_name == "character":
            self._tokenizer = word_tokenizers.CharacterTokenizer()

        if self._tokenizer_name == "whitespace":
            self._tokenizer = word_tokenizers.WhitespaceTokenizer()

        if self._tokenizer_name == "kytea":
            self._tokenizer = word_tokenizers.KyTeaTokenizer(
                with_postag=self._with_postag, model_path=self._model_path,
            )

        if self._tokenizer_name == "sentencepiece":
            if self._model_path is None:
                raise ValueError("`model_path` must be specified for sentencepiece.")

            self._tokenizer = word_tokenizers.SentencepieceTokenizer(model_path=self._model_path,)

        if self._tokenizer_name == "mecab":
            self._tokenizer = word_tokenizers.MeCabTokenizer(
                user_dictionary_path=self._user_dictionary_path,
                system_dictionary_path=self._system_dictionary_path,
                with_postag=self._with_postag,
                dictionary_format=self._dictionary_format,
            )

        if self._tokenizer_name == "janome":
            self._tokenizer = word_tokenizers.JanomeTokenizer(
                user_dictionary_path=self._user_dictionary_path, with_postag=self._with_postag,
            )

        if self._tokenizer_name == "sudachi":
            if self._mode is None:
                raise ValueError("`mode` must be specified for sudachi.")

            self._tokenizer = word_tokenizers.SudachiTokenizer(mode=self._mode, with_postag=self._with_postag,)

        if self._tokenizer_name == "nagisa":
            self._tokenizer = word_tokenizers.NagisaTokenizer(with_postag=self._with_postag,)

    def tokenize(self, text: str) -> List[Token]:
        """Tokenize input text"""

        if isinstance(self._endpoint, str):
            endpoint = self._endpoint
            if not endpoint.startswith("http"):
                endpoint = "http://" + endpoint

            payload = {
                "tokenizer": self._tokenizer_name,
                "model_path": self._model_path,
                "mode": self._mode,
                "text": text,
            }
            headers = {"Content-Type": "application/json"}
            token_params = self._tokenize_with_remote_host(endpoint=endpoint, payload=payload, headers=headers,)

            tokens = []
            for token_param in token_params:
                token = Token.from_dict(token_param)
                tokens.append(token)

            return tokens

        else:
            return self._tokenizer.tokenize(text)

    @staticmethod
    def _tokenize_with_remote_host(endpoint: str, payload: Dict, headers: Dict,) -> List[Dict]:
        return requests.post(endpoint, json=payload, headers=headers,).json()["tokens"][0]

    @property
    def tokenizer(self) -> BaseTokenizer:
        warnings.warn("attribute `tokenizer` will be removed in v5.0.0.")
        return self._tokenizer

    @property
    def name(self) -> str:
        return self._tokenizer.name
