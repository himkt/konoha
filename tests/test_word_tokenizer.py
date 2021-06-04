import json
from typing import Dict, List

import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


@pytest.fixture
def raw_texts():
    data = []
    for line in open("test_fixtures/sentences.txt").readlines():
        data.append(line.rstrip("\n"))
    return data


def read_lines(tokenizer: str, data_type: str):
    data = []
    for tokens_json in open(f"test_fixtures/word_tokenizers/{tokenizer}/{data_type}.jsonl").readlines():
        data.append(json.loads(tokens_json))
    return data


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab"},
        {"tokenizer": "mecab", "with_postag": True},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "sudachi", "mode": "A", "with_postag": True},
        {"tokenizer": "kytea"},
        {"tokenizer": "kytea", "with_postag": True},
        {"tokenizer": "nagisa"},
        {"tokenizer": "nagisa", "with_postag": True},
        {"tokenizer": "janome"},
        {"tokenizer": "janome", "with_postag": True},
        {"tokenizer": "character"},
        {"tokenizer": "whitespace"},
        {"tokenizer": "sentencepiece", "model_path": "data/model.spm"},
    ]
)
def test_tokenize_with_character(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    data_type = "full" if tokenizer_params.get("with_postag", False) else "wakati"
    expect = [Token.from_dict(token_param) for token_param in read_lines(tokenizer_name, data_type)[0]]
    result = tokenizer.tokenize(raw_texts[0])
    assert expect == result


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab"},
        {"tokenizer": "mecab", "with_postag": True},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "sudachi", "mode": "A", "with_postag": True},
        {"tokenizer": "kytea"},
        {"tokenizer": "kytea", "with_postag": True},
        {"tokenizer": "nagisa"},
        {"tokenizer": "nagisa", "with_postag": True},
        {"tokenizer": "janome"},
        {"tokenizer": "janome", "with_postag": True},
        {"tokenizer": "character"},
        {"tokenizer": "whitespace"},
        {"tokenizer": "sentencepiece", "model_path": "data/model.spm"},
    ]
)
def test_batch_tokenize_with_character(raw_texts: List[str], tokenizer_params: Dict):
    tokenizer_name = tokenizer_params["tokenizer"]
    tokenizer = WordTokenizer(**tokenizer_params)
    data_type = "full" if tokenizer_params.get("with_postag", False) else "wakati"
    expect = [
        [Token.from_dict(token_param) for token_param in token_params]
        for token_params in read_lines(tokenizer_name, data_type)
    ]
    result = tokenizer.batch_tokenize(raw_texts)
    assert expect == result
