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


"""
$ kytea
吾輩は猫である
吾輩/名詞/わがはい は/助詞/は 猫/名詞/ねこ で/助動詞/で あ/動詞/あ る/語尾/る
"""


def test_word_tokenize_with_kytea():
    """Test KyTea tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="kytea", with_postag=True)
    except ModuleNotFoundError:
        pytest.skip("skip kytea")

    words = "吾輩 は 猫 で あ る".split(" ")  # NOQA
    postags = "名詞 助詞 名詞 助動詞 動詞 語尾".split(" ")

    expect = [Token(surface=w, postag=p) for w, p in zip(words, postags)]
    result = tokenizer.tokenize(SENTENCE1)
    assert expect == result


"""
$ mecab
我輩は猫である
我輩    名詞,一般,*,*,*,*,我輩,ワガハイ,ワガハイ
は      助詞,係助詞,*,*,*,*,は,ハ,ワ
猫      名詞,一般,*,*,*,*,猫,ネコ,ネコ
で      助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
ある    助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
EOS
"""


def test_word_tokenize_with_mecab():
    """Test MeCab tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="mecab", with_postag=True)
    except ModuleNotFoundError:
        pytest.skip("skip mecab")

    words = "吾輩 は 猫 で ある".split(" ")  # NOQA
    postags = "名詞 助詞 名詞 助動詞 助動詞".split(" ")

    expect = [Token(surface=w, postag=p) for w, p in zip(words, postags)]
    result = tokenizer.tokenize(SENTENCE1)
    assert expect == result


"""
$ pipenv run sudachipy tokenize -m A
医薬品安全管理責任者
医薬    名詞,普通名詞,一般,*,*,*        医薬
品      接尾辞,名詞的,一般,*,*,*        品
安全    名詞,普通名詞,形状詞可能,*,*,*  安全
管理    名詞,普通名詞,サ変可能,*,*,*    管理
責任    名詞,普通名詞,一般,*,*,*        責任
者      接尾辞,名詞的,一般,*,*,*        者
EOS
"""


def test_word_tokenize_with_sudachi_mode_a():
    """Test Sudachi tokenizer."""
    try:
        tokenizer = WordTokenizer(
            tokenizer="sudachi", mode="A", with_postag=True)
    except ModuleNotFoundError:
        pytest.skip("skip sudachi")

    words = "医薬 品 安全 管理 責任 者".split(" ")  # NOQA
    postags = "名詞 接尾辞 名詞 名詞 名詞 接尾辞".split(" ")

    expect = [Token(surface=w, postag=p) for w, p in zip(words, postags)]
    result = tokenizer.tokenize(SENTENCE2)
    assert expect == result
