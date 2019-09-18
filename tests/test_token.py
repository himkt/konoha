"""Test for word tokenizers"""
from tiny_tokenizer.tiny_tokenizer_token import Token


def test_token_without_feature():
    token = Token(surface="大崎")
    assert "大崎" == token.surface
    assert "" == token.feature


def test_token_with_postag():
    token = Token(surface="大崎", postag="名詞")
    assert "大崎" == token.surface
    assert "名詞" == token.feature


def test_token_with_postag2():
    token = Token(
        surface="大崎",
        postag="名詞",
        postag2="固有名詞,人名,姓",
        inflection="*",
        conjugation="*",
        original_form="大崎",
        yomi="オオサキ",
        pron="オーサキ")

    truth = "名詞,固有名詞,人名,姓,*,*,大崎,オオサキ,オーサキ"
    assert token.feature == truth
