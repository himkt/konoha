import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_sudachi_mode_a():
    try:
        import sudachipy
        del sudachipy
    except ImportError:
        pytest.skip("SudachiPy is not installed.")

    tokenizer = WordTokenizer(tokenizer="Sudachi", mode="A")
    expect = [Token(surface=w) for w in "医薬 品 安全 管理 責任 者".split(" ")]
    result = tokenizer.tokenize("医薬品安全管理責任者")
    assert expect == result


def test_word_tokenize_with_sudachi_mode_b():
    try:
        import sudachipy
        del sudachipy
    except ImportError:
        pytest.skip("SudachiPy is not installed.")

    tokenizer = WordTokenizer(tokenizer="Sudachi", mode="B")
    expect = [Token(surface=w) for w in "医薬品 安全 管理 責任者".split(" ")]
    result = tokenizer.tokenize("医薬品安全管理責任者")
    assert expect == result


def test_word_tokenize_with_sudachi_mode_c():
    try:
        import sudachipy
        del sudachipy
    except ImportError:
        pytest.skip("SudachiPy is not installed.")

    tokenizer = WordTokenizer(tokenizer="Sudachi", mode="C")
    expect = [Token(surface=w) for w in "医薬品 安全 管理責任者".split(" ")]
    result = tokenizer.tokenize("医薬品安全管理責任者")
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


def test_postagging_with_sudachi_mode_a():
    """Test Sudachi tokenizer."""
    try:
        tokenizer = WordTokenizer(
            tokenizer="sudachi", mode="A", with_postag=True)
    except ImportError:
        pytest.skip("SudachiPy is not installed.")

    expect = [Token(**kwargs) for kwargs in sudachi_tokens_list]
    result = tokenizer.tokenize("医薬品安全管理責任者")
    assert expect == result
