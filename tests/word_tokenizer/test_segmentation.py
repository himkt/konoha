import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenizer():
    tokenizer1 = WordTokenizer(tokenizer="Whitespace")
    tokenizer2 = WordTokenizer(tokenizer="whitespace")
    assert tokenizer1.tokenizer.name == tokenizer2.tokenizer.name


def test_word_tokenize_with_kytea():
    try:
        import Mykytea
        del Mykytea
    except ImportError:
        pytest.skip("skip kytea")

    tokenizer = WordTokenizer(tokenizer="KyTea")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で あ る".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_kytea_using_custom_model():
    try:
        import Mykytea
        del Mykytea
    except ImportError:
        pytest.skip("skip kytea")

    tokenizer = WordTokenizer(tokenizer="KyTea", model_path="data/model.knm")
    expect = [Token(surface=w) for w in "吾輩は 猫である".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_mecab():
    try:
        import natto
        del natto
    except ImportError:
        pytest.skip("natto-py is not installed")

    tokenizer = WordTokenizer(tokenizer="MeCab")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_janome():
    try:
        import janome
        del janome
    except ImportError:
        pytest.skip("janome is not installed")

    tokenizer = WordTokenizer(tokenizer="Janome")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_mecab_whitespace():
    try:
        import natto
        del natto
    except ImportError:
        pytest.skip("natto-py is not installed")

    tokenizer = WordTokenizer(tokenizer="MeCab")
    expect = [Token(surface=w) for w in "吾輩 は 　 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は　である")
    assert expect == result


def test_word_tokenize_with_sentencepiece():
    try:
        import sentencepiece
        del sentencepiece
    except ImportError:
        pytest.skip("sentencepiece is not installed")

    tokenizer = WordTokenizer(
        tokenizer="Sentencepiece",
        model_path="data/model.spm"
    )
    expect = [Token(surface=w) for w in "▁ 吾 輩 は 猫 である".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_sudachi_mode_a():
    try:
        import sudachipy
        del sudachipy
    except ImportError:
        pytest.skip("sudachipy is not installed")

    tokenizer = WordTokenizer(tokenizer="Sudachi", mode="A")
    expect = [Token(surface=w) for w in "医薬 品 安全 管理 責任 者".split(" ")]
    result = tokenizer.tokenize("医薬品安全管理責任者")
    assert expect == result


def test_word_tokenize_with_sudachi_mode_b():
    try:
        import sudachipy
        del sudachipy
    except ImportError:
        pytest.skip("sudachipy is not installed")

    tokenizer = WordTokenizer(tokenizer="Sudachi", mode="B")
    expect = [Token(surface=w) for w in "医薬品 安全 管理 責任者".split(" ")]
    result = tokenizer.tokenize("医薬品安全管理責任者")
    assert expect == result


def test_word_tokenize_with_sudachi_mode_c():
    try:
        import sudachipy
        del sudachipy
    except ImportError:
        pytest.skip("sudachipy is not installed")

    tokenizer = WordTokenizer(tokenizer="Sudachi", mode="C")
    expect = [Token(surface=w) for w in "医薬品 安全 管理責任者".split(" ")]
    result = tokenizer.tokenize("医薬品安全管理責任者")
    assert expect == result


def test_word_tokenize_with_character():
    tokenizer = WordTokenizer(tokenizer="Character")
    expect = [Token(surface=w) for w in "吾 輩 は 猫 で あ る".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_whitespace():
    tokenizer = WordTokenizer(tokenizer="Whitespace")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩 は 猫 で ある")
    assert expect == result
