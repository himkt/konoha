import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer

SENTENCE1 = "吾輩は猫である"


def test_kytea_with_s3_model():
    try:
        import boto3
        del boto3
    except ImportError:
        pytest.skip("skip s3 test because of missing boto3")

    try:
        tokenizer = WordTokenizer(
            tokenizer="KyTea",
            model_path="s3://konoha-demo/kytea/model.knm"
        )
    except ImportError:
        pytest.skip("skip kytea")

    expect = [Token(surface=w) for w in "吾輩は 猫である".split(" ")]  # NOQA
    result = tokenizer.tokenize(SENTENCE1)
    assert expect == result


def test_sentencepiece_with_s3_model():
    try:
        import boto3
        del boto3
    except ImportError:
        pytest.skip("skip s3 test because of missing boto3")

    try:
        tokenizer = WordTokenizer(
            tokenizer="SentencePiece",
            model_path="s3://konoha-demo/sentencepiece/model.spm"
        )
    except ImportError:
        pytest.skip("skip sentencepiece")

    expect = [Token(surface=w) for w in "▁ 吾 輩 は 猫 である".split(" ")]  # NOQA
    result = tokenizer.tokenize(SENTENCE1)
    assert expect == result
