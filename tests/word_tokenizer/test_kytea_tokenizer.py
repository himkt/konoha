import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_kytea():
    try:
        import Mykytea

        del Mykytea
    except ImportError:
        pytest.skip("KyTea is not installed.")

    tokenizer = WordTokenizer(tokenizer="KyTea")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で あ る".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_kytea_using_custom_model():
    try:
        import Mykytea

        del Mykytea
    except ImportError:
        pytest.skip("KyTea is not installed.")

    tokenizer = WordTokenizer(tokenizer="KyTea", model_path="data/model.knm")
    expect = [Token(surface=w) for w in "吾輩は 猫である".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


"""
$ kytea
吾輩は猫である
吾輩/名詞/わがはい は/助詞/は 猫/名詞/ねこ で/助動詞/で あ/動詞/あ る/語尾/る
"""
kytea_tokens_list = [
    {"surface": "吾輩", "postag": "名詞", "pron": "わがはい"},
    {"surface": "は", "postag": "助詞", "pron": "は"},
    {"surface": "猫", "postag": "名詞", "pron": "ねこ"},
    {"surface": "で", "postag": "助動詞", "pron": "で"},
    {"surface": "あ", "postag": "動詞", "pron": "あ"},
    {"surface": "る", "postag": "語尾", "pron": "る"},
]


def test_postagging_with_kytea():
    """Test KyTea tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="kytea", with_postag=True)
    except ImportError:
        pytest.skip("KyTea is not installed.")

    expect = [Token(**kwargs) for kwargs in kytea_tokens_list]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_kytea_with_s3_model():
    try:
        import boto3

        del boto3
    except ImportError:
        pytest.skip("skip s3 test because of missing boto3")

    try:
        tokenizer = WordTokenizer(
            tokenizer="KyTea", model_path="s3://konoha-demo/kytea/model.knm"
        )
    except ImportError:
        pytest.skip("KyTea is not installed.")

    expect = [Token(surface=w) for w in "吾輩は 猫である".split(" ")]  # NOQA
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result
