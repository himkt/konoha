"""Test for word tokenizers"""
import unittest
import pytest

from tiny_tokenizer.word_tokenizer import WordTokenizer
from tiny_tokenizer.token import Token


SENTENCE1 = "吾輩は猫である"
SENTENCE2 = "医薬品安全管理責任者"


class PostaggingTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="kytea",
                with_postag=True,
            )
        except ModuleNotFoundError:
            pytest.skip("skip kytea")

        words   = "吾輩 は 猫 で あ る".split(" ")  # NOQA
        postags = "名詞 助詞 名詞 助動詞 動詞 語尾".split(" ")

        expect = [Token(surface=w, postag=p) for w, p in zip(words, postags)]
        result = tokenizer.tokenize(SENTENCE1)
        assert expect == result

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="mecab",
                with_postag=True,
            )
        except ModuleNotFoundError:
            pytest.skip("skip mecab")

        words   = "吾輩 は 猫 で ある".split(" ")  # NOQA
        postags = "名詞 助詞 名詞 助動詞 助動詞".split(" ")

        expect = [Token(surface=w, postag=p) for w, p in zip(words, postags)]
        result = tokenizer.tokenize(SENTENCE1)
        assert expect == result

    def test_word_tokenize_with_sudachi_mode_a(self):
        """Test Sudachi tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="sudachi",
                mode="A",
                with_postag=True,
            )
        except ModuleNotFoundError:
            pytest.skip("skip sudachi")

        words   = "医薬 品 安全 管理 責任 者".split(" ")  # NOQA
        postags = "名詞 接尾辞 名詞 名詞 名詞 接尾辞".split(" ")

        expect = [Token(surface=w, postag=p) for w, p in zip(words, postags)]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)
