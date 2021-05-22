import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_mecab():
    try:
        import natto

        del natto
    except ImportError:
        pytest.skip("natto-py is not installed.")

    tokenizer = WordTokenizer(tokenizer="MeCab")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_mecab_whitespace():
    try:
        import natto

        del natto
    except ImportError:
        pytest.skip("natto-py is not installed.")

    tokenizer = WordTokenizer(tokenizer="MeCab")
    expect = [Token(surface=w) for w in "吾輩 は 　 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は　である")
    assert expect == result


"""
$ mecab
吾輩は猫である
吾輩    名詞,一般,*,*,*,*,吾輩,ワガハイ,ワガハイ
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
猫      名詞,一般,*,*,*,*,猫,ネコ,ネコ
で      助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
ある    助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
EOS
"""
mecab_tokens_list = [
    {
        "surface": "吾輩",
        "postag": "名詞",
        "postag2": "代名詞",
        "postag3": "一般",
        "postag4": "*",
        "inflection": "*",
        "conjugation": "*",
        "base_form": None,
        "normalized_form": None,
        "yomi": "ワガハイ",
        "pron": "ワガハイ",
    },  # NOQA
    {
        "surface": "は",
        "postag": "助詞",
        "postag2": "係助詞",
        "postag3": "*",
        "postag4": "*",
        "inflection": "*",
        "conjugation": "*",
        "base_form": None,
        "normalized_form": None,
        "yomi": "ハ",
        "pron": "ワ",
    },  # NOQA
    {
        "surface": "猫",
        "postag": "名詞",
        "postag2": "一般",
        "postag3": "*",
        "postag4": "*",
        "inflection": "*",
        "conjugation": "*",
        "base_form": None,
        "normalized_form": None,
        "yomi": "ネコ",
        "pron": "ネコ",
    },  # NOQA
    {
        "surface": "で",
        "postag": "助動詞",
        "postag2": "*",
        "postag3": "*",
        "postag4": "*",
        "inflection": "特殊・ダ",
        "conjugation": "連用形",
        "base_form": None,
        "normalized_form": None,
        "yomi": "デ",
        "pron": "デ",
    },  # NOQA
    {
        "surface": "ある",
        "postag": "助動詞",
        "postag2": "*",
        "postag3": "*",
        "postag4": "*",
        "inflection": "五段・ラ行アル",
        "conjugation": "基本形",
        "base_form": None,
        "normalized_form": None,
        "yomi": "アル",
        "pron": "アル",
    },  # NOQA
]


def test_postagging_with_mecab():
    """Test MeCab tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="mecab", with_postag=True)
    except ImportError:
        pytest.skip("natto-py is not installed.")

    expect = [Token(**kwargs) for kwargs in mecab_tokens_list]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


def test_word_tokenize_with_s3_system_dictionary():
    try:
        import natto

        del natto
    except ImportError:
        pytest.skip("natto-py is not installed.")

    tokenizer = WordTokenizer(
        tokenizer="MeCab",
        system_dictionary_path="s3://konoha-demo/mecab/ipadic",
    )
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result
