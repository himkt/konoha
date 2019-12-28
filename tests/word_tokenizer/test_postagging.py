"""Test for word tokenizers.

Note that it uses the full version of
SudachiPy dictionary.

URL is following:
    'https://object-storage.tyo2.conoha.io/' \
    'v1/nc_2520839e1f9641b08211a5c85243124a/' \
    'sudachi/sudachi-dictionary-20190718-full.zip'
"""

import pytest

from tiny_tokenizer.tiny_tokenizer_token import Token
from tiny_tokenizer.word_tokenizer import WordTokenizer

SENTENCE1 = "吾輩は猫である"
SENTENCE2 = "医薬品安全管理責任者"
SENTENCE3 = "すもももももももものうち"


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


def test_word_tokenize_with_kytea():
    """Test KyTea tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="kytea", with_postag=True)
    except ImportError:
        pytest.skip("skip kytea")

    expect = [Token(**kwargs) for kwargs in kytea_tokens_list]
    result = tokenizer.tokenize(SENTENCE1)
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
    {"surface": "吾輩", "postag": "名詞", "postag2": "代名詞", "postag3": "一般", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": None, "normalized_form": None, "yomi": "ワガハイ", "pron": "ワガハイ"},  # NOQA
    {"surface": "は", "postag": "助詞", "postag2": "係助詞", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": None, "normalized_form": None, "yomi": "ハ", "pron": "ワ"},  # NOQA
    {"surface": "猫", "postag": "名詞", "postag2": "一般", "postag3": "*", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": None, "normalized_form": None, "yomi": "ネコ", "pron": "ネコ"},  # NOQA
    {"surface": "で", "postag": "助動詞", "postag2": "*", "postag3": "*", "postag4": "*", "inflection": "特殊・ダ", "conjugation": "連用形", "base_form": None, "normalized_form": None, "yomi": "デ", "pron": "デ"},  # NOQA
    {"surface": "ある", "postag": "助動詞", "postag2": "*", "postag3": "*", "postag4": "*", "inflection": "五段・ラ行アル", "conjugation": "基本形", "base_form": None, "normalized_form": None, "yomi": "アル", "pron": "アル"},  # NOQA
]


def test_word_tokenize_with_mecab():
    """Test MeCab tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="mecab", with_postag=True)
    except ImportError:
        pytest.skip("skip mecab")

    expect = [Token(**kwargs) for kwargs in mecab_tokens_list]
    result = tokenizer.tokenize(SENTENCE1)
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


def test_word_tokenize_with_janome():
    """Test MeCab tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="janome", with_postag=True)
    except ImportError:
        pytest.skip("skip janome")

    expect = [Token(**kwargs) for kwargs in janome_tokens_list]
    result = tokenizer.tokenize(SENTENCE3)
    assert expect == result


"""
$ pipenv run sudachipy tokenize -m A -a
医薬品安全管理責任者
医薬    名詞,普通名詞,一般,*,*,*        医薬    医薬    イヤク  0       (OOV)
品      接尾辞,名詞的,一般,*,*,*        品      品      ヒン    0       (OOV)
安全    名詞,普通名詞,形状詞可能,*,*,*  安全    安全    アンゼン        0       (OOV)
管理    名詞,普通名詞,サ変可能,*,*,*    管理    管理    カンリ  0       (OOV)
責任    名詞,普通名詞,一般,*,*,*        責任    責任    セキニン        0       (OOV)
者      接尾辞,名詞的,一般,*,*,*        者      者      シャ    0       (OOV)
EOS
                                        ^^^^    ^^^^    ^^^^^^^^
                                        norm    dict      yomi
"""
sudachi_tokens_list = [
    {"surface": "医薬", "postag": "名詞", "postag2": "普通名詞", "postag3": "一般", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "医薬", "normalized_form": "医薬", "yomi": "イヤク", "pron": None},  # NOQA
    {"surface": "品", "postag": "接尾辞", "postag2": "名詞的", "postag3": "一般", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "品", "normalized_form": "品", "yomi": "ヒン", "pron": None},  # NOQA
    {"surface": "安全", "postag": "名詞", "postag2": "普通名詞", "postag3": "形状詞可能", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "安全", "normalized_form": "安全", "yomi": "アンゼン", "pron": None},  # NOQA
    {"surface": "管理", "postag": "名詞", "postag2": "普通名詞", "postag3": "サ変可能", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "管理", "normalized_form": "管理", "yomi": "カンリ", "pron": None},  # NOQA
    {"surface": "責任", "postag": "名詞", "postag2": "普通名詞", "postag3": "一般", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "責任", "normalized_form": "責任", "yomi": "セキニン", "pron": None},  # NOQA
    {"surface": "者", "postag": "接尾辞", "postag2": "名詞的", "postag3": "一般", "postag4": "*", "inflection": "*", "conjugation": "*", "base_form": "者", "normalized_form": "者", "yomi": "シャ", "pron": None},  # NOQA
]


def test_word_tokenize_with_sudachi_mode_a():
    """Test Sudachi tokenizer."""
    try:
        tokenizer = WordTokenizer(
            tokenizer="sudachi", mode="A", with_postag=True)
    except ImportError:
        pytest.skip("skip sudachi")

    expect = [Token(**kwargs) for kwargs in sudachi_tokens_list]
    result = tokenizer.tokenize(SENTENCE2)
    assert expect == result
