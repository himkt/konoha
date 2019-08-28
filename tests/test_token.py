"""Test for word tokenizers"""
import unittest

from tiny_tokenizer.tiny_tokenizer_token import Token


class TokenTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_token_without_feature(self):
        token = Token(surface="大崎")
        self.assertEqual("大崎", token.surface)
        self.assertEqual("", token.feature)

    def test_token_with_postag(self):
        token = Token(surface="大崎", postag="名詞")
        self.assertEqual("大崎", token.surface)
        self.assertEqual("名詞", token.feature)

    def test_token_with_postag2(self):
        token = Token(
            surface="大崎",
            postag="名詞",
            postag2="固有名詞,人名,姓",
            conj_type="*",
            conj_form="*",
            origin_form="大崎",
            yomi="オオサキ",
            pron="オーサキ")

        self.assertEqual(
            "名詞,固有名詞,人名,姓,*,*,大崎,オオサキ,オーサキ",
            token.feature)
