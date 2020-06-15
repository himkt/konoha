import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_sentencepiece():
    try:
        import sentencepiece

        del sentencepiece
    except ImportError:
        pytest.skip("Sentencepiece is not installed.")

    tokenizer = WordTokenizer(tokenizer="Sentencepiece", model_path="data/model.spm")
    expect = [Token(surface=w) for w in "▁ 吾 輩 は 猫 である".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
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
            model_path="s3://konoha-demo/sentencepiece/model.spm",
        )
    except ImportError:
        pytest.skip("Sentencepiece is not installed.")

    expect = [Token(surface=w) for w in "▁ 吾 輩 は 猫 である".split(" ")]  # NOQA
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result
