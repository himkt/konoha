import json
from typing import Dict
from typing import List

import pytest

from konoha.data.token import Token
from konoha import WordTokenizer


@pytest.fixture
def raw_texts():
    data = []
    for line in open("test_fixtures/sentences.txt").readlines():
        data.append(line.rstrip("\n"))
    return data


def read_lines(tokenizer: str):
    data = []
    for tokens_json in open(f"test_fixtures/word_tokenizers/{tokenizer}.jsonl").readlines():
        data.append(json.loads(tokens_json))
    return data


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab", "system_dictionary_path": "s3://konoha-demo/mecab/ipadic"},
    ]
)
def test_tokenize(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    expect = [Token.from_dict(token_param) for token_param in read_lines(tokenizer_name)[0]]
    result = tokenizer.tokenize(raw_texts[0])
    assert expect == result


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab", "system_dictionary_path": "s3://konoha-demo/mecab/ipadic"},
    ]
)
def test_batch_tokenize(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    expect = [
        [Token.from_dict(token_param) for token_param in token_params]
        for token_params in read_lines(tokenizer_name)
    ]
    result = tokenizer.batch_tokenize(raw_texts)
    assert expect == result
