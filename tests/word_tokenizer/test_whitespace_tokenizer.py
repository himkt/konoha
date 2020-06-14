from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_whitespace():
    tokenizer = WordTokenizer(tokenizer="Whitespace")
    expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
    result = tokenizer.tokenize("吾輩 は 猫 で ある")
    assert expect == result
