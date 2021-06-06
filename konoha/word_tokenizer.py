"""Word Level Tokenizer."""
import warnings
from typing import Dict
from typing import List
from typing import Optional

import requests

from konoha import word_tokenizers
from konoha.data.resource import Resource
from konoha.data.token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class WordTokenizer:
    def __init__(
        self,
        tokenizer: str = "MeCab",
        user_dictionary_path: Optional[str] = None,
        system_dictionary_path: Optional[str] = None,
        model_path: Optional[str] = None,
        mode: Optional[str] = None,
        dictionary_format: Optional[str] = None,
        endpoint: Optional[str] = None,
        ssl: Optional[bool] = None,
        port: Optional[int] = None,
    ) -> None:
        user_dictionary = Resource(user_dictionary_path)
        system_dictionary = Resource(system_dictionary_path)
        model = Resource(model_path)

        self._tokenizer_name = tokenizer.lower()
        self._user_dictionary_path = user_dictionary.path
        self._system_dictionary_path = system_dictionary.path
        self._model_path = model.path
        self._mode = mode.lower() if mode is not None else None
        self._dictionary_format = dictionary_format
        self._tokenizer: Optional[BaseTokenizer] = None
        self._endpoint = endpoint
        self._ssl = ssl
        self._port = port

        if not isinstance(endpoint, str):
            self._setup_tokenizer()

    def _setup_tokenizer(self) -> None:
        if self._tokenizer_name == "character":
            self._tokenizer = word_tokenizers.CharacterTokenizer()

        if self._tokenizer_name == "whitespace":
            self._tokenizer = word_tokenizers.WhitespaceTokenizer()

        if self._tokenizer_name == "kytea":
            self._tokenizer = word_tokenizers.KyTeaTokenizer(model_path=self._model_path)

        if self._tokenizer_name == "sentencepiece":
            if self._model_path is None:
                raise ValueError("`model_path` must be specified for sentencepiece.")

            self._tokenizer = word_tokenizers.SentencepieceTokenizer(model_path=self._model_path)

        if self._tokenizer_name == "mecab":
            self._tokenizer = word_tokenizers.MeCabTokenizer(
                user_dictionary_path=self._user_dictionary_path,
                system_dictionary_path=self._system_dictionary_path,
                dictionary_format=self._dictionary_format,
            )

        if self._tokenizer_name == "janome":
            self._tokenizer = word_tokenizers.JanomeTokenizer(user_dictionary_path=self._user_dictionary_path)

        if self._tokenizer_name == "sudachi":
            if self._mode is None:
                raise ValueError("`mode` must be specified for sudachi.")

            self._tokenizer = word_tokenizers.SudachiTokenizer(mode=self._mode)

        if self._tokenizer_name == "nagisa":
            self._tokenizer = word_tokenizers.NagisaTokenizer()

    def tokenize(self, text: str) -> List[Token]:
        """Tokenize input text"""

        if isinstance(self._endpoint, str):
            endpoint = self.get_endpoint("/api/v1/tokenize")
            payload = dict(self.payload, text=text)
            token_params = self._tokenize_with_remote_host(endpoint=endpoint, payload=payload, headers=self.headers)
            return [Token.from_dict(token_param) for token_param in token_params]

        else:
            assert self._tokenizer is not None
            return self._tokenizer.tokenize(text)

    def batch_tokenize(self, texts: List[str]) -> List[List[Token]]:
        """Tokenize input texts"""

        if isinstance(self._endpoint, str):
            endpoint = self.get_endpoint("/api/v1/batch_tokenize")
            payload = dict(self.payload, texts=texts)
            token_params_list = self._batch_tokenize_with_remote_host(
                endpoint=endpoint,
                payload=payload,
                headers=self.headers,
            )

            tokens_list: List[List[Token]] = []
            for tokens in token_params_list:
                tokens_list.append([Token.from_dict(token) for token in tokens])

            return tokens_list

        else:
            assert self._tokenizer is not None
            return [self._tokenizer.tokenize(text) for text in texts]

    @staticmethod
    def _tokenize_with_remote_host(endpoint: str, payload: Dict, headers: Dict) -> List[Dict]:
        return requests.post(endpoint, json=payload, headers=headers).json()["tokens"]

    @staticmethod
    def _batch_tokenize_with_remote_host(endpoint: str, payload: Dict, headers: Dict) -> List[List[Dict]]:
        return requests.post(endpoint, json=payload, headers=headers).json()["tokens_list"]

    @property
    def tokenizer(self) -> BaseTokenizer:
        warnings.warn("attribute `tokenizer` will be removed in v5.0.0.")
        assert self._tokenizer is not None
        return self._tokenizer

    @property
    def name(self) -> str:
        assert self._tokenizer is not None
        return self._tokenizer.name

    def get_endpoint(self, method: str):
        assert self._endpoint
        endpoint = self._endpoint

        if self._ssl and not endpoint.startswith("https://"):
            endpoint = "https://" + endpoint

        if not self._ssl and not endpoint.startswith("http://"):
            endpoint = "http://" + endpoint

        return endpoint + method

    @property
    def payload(self):
        return {
            "tokenizer": self._tokenizer_name,
            "user_dictionary_path": self._user_dictionary_path,
            "system_dictionary_path": self._system_dictionary_path,
            "model_path": self._model_path,
            "mode": self._mode,
            "dictionary_format": self._dictionary_format,
        }

    @property
    def headers(self):
        return {"Content-Type": "application/json"}
