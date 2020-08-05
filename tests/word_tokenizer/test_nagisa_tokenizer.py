import pytest

from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_nagisa():
    try:
        import nagisa
        del nagisa
    except ImportError:
        pytest.skip("nagisa is not installed.")

    tokenizer = WordTokenizer(tokenizer="nagisa")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result


"""
>>> import nagisa
[dynet] random seed: 1234
[dynet] allocating memory: 32MB
[dynet] memory allocation done.
>>> text = '吾輩は猫である'
>>> words = nagisa.tagging(text)
>>> print(words)
吾輩/代名詞 は/助詞 猫/名詞 で/助動詞 ある/動詞
>>> # Get a list of words
... print(words.words)
['吾輩', 'は', '猫', 'で', 'ある']
>>> # Get a list of POS-tags
... print(words.postags)
['代名詞', '助詞', '名詞', '助動詞', '動詞']
"""
nagisa_tokens_list = [
    {"surface": "吾輩", "postag": "代名詞"},
    {"surface": "は", "postag": "助詞"},
    {"surface": "猫", "postag": "名詞"},
    {"surface": "で", "postag": "助動詞"},
    {"surface": "ある", "postag": "動詞"},
]


def test_postagging_with_nagisa():
    """Test nagisa tokenizer."""
    try:
        tokenizer = WordTokenizer(tokenizer="nagisa", with_postag=True)
    except ImportError:
        pytest.skip("nagisa is not installed.")

    expect = [Token(**kwargs) for kwargs in nagisa_tokens_list]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result
