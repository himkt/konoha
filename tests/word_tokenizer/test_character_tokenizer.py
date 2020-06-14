from konoha.konoha_token import Token
from konoha.word_tokenizer import WordTokenizer


def test_word_tokenize_with_character():
    tokenizer = WordTokenizer(tokenizer="Character")
    expect = [Token(surface=w) for w in "吾 輩 は 猫 で あ る".split(" ")]
    result = tokenizer.tokenize("吾輩は猫である")
    assert expect == result
