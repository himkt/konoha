import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_janome():
    try:
        import janome
        del janome
    except ImportError:
        pytest.skip("Janome is not installed.")

    tokenizer = WordTokenizer(tokenizer="Janome")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


"""
(env) $ python
>>> from janome.tokenizer import Tokenizer
>>> t = Tokenizer()
>>> for token in t.tokenize(u'すもももももももものうち'):
...     print(token)
...
すもも 名詞,一般,*,*,*,*,すもも,スモモ,スモモ
も    助詞,係助詞,*,*,*,*,も,モ,モ
もも  名詞,一般,*,*,*,*,もも,モモ,モモ
も    助詞,係助詞,*,*,*,*,も,モ,モ
もも  名詞,一般,*,*,*,*,もも,モモ,モモ
の    助詞,連体化,*,*,*,*,の,ノ,ノ
うち  名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ
"""
janome_tokens_list = [
    {"surface": "すもも", "postag": "名詞", "postag2": "一般", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "すもも", "normalized_form": None, "yomi": "スモモ", "pron": "スモモ"},  # NOQA
    {"surface": "も", "postag": "助詞", "postag2": "係助詞", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "も", "normalized_form": None, "yomi": "モ", "pron": "モ"},  # NOQA
    {"surface": "もも", "postag": "名詞", "postag2": "一般", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "もも", "normalized_form": None, "yomi": "モモ", "pron": "モモ"},  # NOQA
    {"surface": "も", "postag": "助詞", "postag2": "係助詞", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "も", "normalized_form": None, "yomi": "モ", "pron": "モ"},  # NOQA
    {"surface": "もも", "postag": "名詞", "postag2": "一般", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "もも", "normalized_form": None, "yomi": "モモ", "pron": "モモ"},  # NOQA
    {"surface": "の", "postag": "助詞", "postag2": "連体化", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "の", "normalized_form": None, "yomi": "ノ", "pron": "ノ"},  # NOQA
    {"surface": "うち", "postag": "名詞", "postag2": "非自立", "postag3": "副詞可能", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "うち", "normalized_form": None, "yomi": "ウチ", "pron": "ウチ"},  # NOQA
]


def test_postagging_with_janome():
    """Test MeCab tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="janome", with_postag=True)
    except ImportError:
        pytest.skip("Janome is not installed.")

    expect = [Token(**kwargs) for kwargs in janome_tokens_list]
    result = tokenizer.tokenize("すもももももももものうち")
    assert expect == result
