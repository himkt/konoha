from konoha.word_tokenizer import WordTokenizer


def test_word_tokenizer():
    tokenizer1 = WordTokenizer(tokenizer="Whitespace")
    tokenizer2 = WordTokenizer(tokenizer="whitespace")
    assert tokenizer1.tokenizer.name == tokenizer2.tokenizer.name
