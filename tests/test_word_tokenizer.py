import json
import os
from typing import Dict
from typing import List
import sys

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
    "tokenizer_params",
    [
        {"tokenizer": "mecab"},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "kytea"},
        {"tokenizer": "nagisa"},
        {"tokenizer": "janome"},
        {"tokenizer": "character"},
        {"tokenizer": "whitespace"},
        {"tokenizer": "sentencepiece", "model_path": "data/model.spm"},
    ],
)
def test_tokenize_with_character(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    expect = [Token.from_dict(token_param) for token_param in read_lines(tokenizer_name)[0]]
    result = tokenizer.tokenize(raw_texts[0])
    assert expect == result


@pytest.mark.parametrize(
    "tokenizer_params",
    [
        {"tokenizer": "mecab", "system_dictionary_path": "s3://konoha-demo/mecab/ipadic"},
    ],
)
def test_tokenize(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    expect = [Token.from_dict(token_param) for token_param in read_lines(tokenizer_name)[0]]
    result = tokenizer.tokenize(raw_texts[0])
    assert expect == result


@pytest.mark.parametrize(
    "tokenizer_params",
    [
        {"tokenizer": "mecab"},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "kytea"},
        {"tokenizer": "nagisa"},
        {"tokenizer": "janome"},
        {"tokenizer": "character"},
        {"tokenizer": "whitespace"},
        {"tokenizer": "sentencepiece", "model_path": "data/model.spm"},
    ],
)
def test_batch_tokenize_with_character(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    expect = [
        [Token.from_dict(token_param) for token_param in token_params] for token_params in read_lines(tokenizer_name)
    ]
    result = tokenizer.batch_tokenize(raw_texts)
    assert expect == result


@pytest.mark.parametrize(
    "tokenizer_params",
    [
        {"tokenizer": "mecab", "system_dictionary_path": "s3://konoha-demo/mecab/ipadic"},
    ],
)
def test_batch_tokenize(raw_texts: List[str], tokenizer_params: Dict):
    if "AWS_ACCESS_KEY_ID" not in os.environ and tokenizer_params["system_dictionary_path"].startswith("s3://"):
        pytest.skip("AWS credentials not found.")

    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    expect = [
        [Token.from_dict(token_param) for token_param in token_params] for token_params in read_lines(tokenizer_name)
    ]
    result = tokenizer.batch_tokenize(raw_texts)
    assert expect == result


@pytest.mark.parametrize(
    "text,expect",
    [
        ("私 は猫", [("私 ", "UNK", "UNK"), ("は", "助詞", "は"), ("猫", "名詞", "ねこ")]),
        (
            "a/b です",
            [
                ("a", "UNK", "UNK"),
                ("/", "UNK", "UNK"),
                ("b", "UNK", "UNK"),
                (" ", "UNK", "UNK"),
                ("で", "助動詞", "で"),
                ("す", "語尾", "す"),
            ],
        ),
    ],
)
def test_kytea_tokenize_with_space_and_slash(text: str, expect: List):
    tokenizer = WordTokenizer("kytea", model_path="data/model.knm")
    result = [(token.surface, token.postag, token.pron) for token in tokenizer.tokenize(text)]
    assert expect == result
