"""Test for word tokenizers"""
import unittest
import pytest

from tiny_tokenizer.word_tokenizer import WordTokenizer
from tiny_tokenizer.word_tokenizer import Token


SENTENCE1 = "吾輩は猫である"
SENTENCE2 = "医薬品安全管理責任者"


class WordTokenizerTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="KyTea")
        except ModuleNotFoundError:
            pytest.skip("skip kytea")

        expect = [Token(surface=w) for w in "吾輩 は 猫 で あ る".split(" ")]
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="MeCab")
        except ModuleNotFoundError:
            pytest.skip("skip mecab")

        expect = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sentencepiece(self):
        """Test Sentencepiece tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="Sentencepiece",
                model_path="data/model.spm"
            )
        except ModuleNotFoundError:
            pytest.skip("skip sentencepiece")

        expect = [Token(surface=w) for w in "▁ 吾 輩 は 猫 である".split(" ")]
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sudachi_mode_a(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer(
            tokenizer="Sudachi",
            mode="A",
        )
        expect = [Token(surface=w) for w in "医薬 品 安全 管理 責任 者".split(" ")]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sudachi_mode_b(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer(
            tokenizer="Sudachi",
            mode="B",
        )
        expect = [Token(surface=w) for w in "医薬品 安全 管理 責任者".split(" ")]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sudachi_mode_c(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer(
            tokenizer="Sudachi",
            mode="C",
        )
        expect = [Token(surface=w) for w in "医薬品安全管理責任者".split(" ")]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_character(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer(
            tokenizer="Character"
        )
        expect = [Token(surface=w) for w in "吾 輩 は 猫 で あ る".split(" ")]
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_using_lowercase(self):
        """Test KyTea tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="kytea")
        except ModuleNotFoundError:
            pytest.skip("skip kytea")

        expect = [Token(surface=w) for w in "吾輩 は 猫 で あ る".split(" ")]
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)
