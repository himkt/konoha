"""Test for word tokenizers"""
import unittest
import pytest

from tiny_tokenizer.word_tokenizer import WordTokenizer
from tiny_tokenizer.token import Token


SENTENCE1 = "吾輩は猫である"
SENTENCE2 = "医薬品安全管理責任者"


class WordSegmentationTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        try:
            tokenizer1 = WordTokenizer(tokenizer="KyTea")
            tokenizer2 = WordTokenizer(tokenizer="kytea")
        except ModuleNotFoundError:
            pytest.skip("skip kytea")

        expect  = [Token(surface=w) for w in "吾輩 は 猫 で あ る".split(" ")]  # NOQA
        result1 = tokenizer1.tokenize(SENTENCE1)
        result2 = tokenizer2.tokenize(SENTENCE1)
        assert expect  == result1  # NOQA
        assert result1 == result2

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        try:
            tokenizer1 = WordTokenizer(tokenizer="MeCab")
            tokenizer2 = WordTokenizer(tokenizer="mecab")
        except ModuleNotFoundError:
            pytest.skip("skip mecab")

        expect  = [Token(surface=w) for w in "吾輩 は 猫 で ある".split(" ")]  # NOQA
        result1 = tokenizer1.tokenize(SENTENCE1)
        result2 = tokenizer2.tokenize(SENTENCE1)
        assert expect  == result1  # NOQA
        assert result1 == result2

    def test_word_tokenize_with_sentencepiece(self):
        """Test Sentencepiece tokenizer."""
        try:
            tokenizer1 = WordTokenizer(
                tokenizer="Sentencepiece",
                model_path="data/model.spm"
            )
            tokenizer2 = WordTokenizer(
                tokenizer="Sentencepiece",
                model_path="data/model.spm"
            )
        except ModuleNotFoundError:
            pytest.skip("skip sentencepiece")

        expect = [Token(surface=w) for w in "▁ 吾 輩 は 猫 である".split(" ")]  # NOQA
        result1 = tokenizer1.tokenize(SENTENCE1)
        result2 = tokenizer2.tokenize(SENTENCE1)
        assert expect  == result1  # NOQA
        assert result1 == result2

    def test_word_tokenize_with_sudachi_mode_a(self):
        """Test Sudachi tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="Sudachi",
                mode="A",
            )
        except ModuleNotFoundError:
            pytest.skip("skip sudachi")

        expect = [Token(surface=w) for w in "医薬 品 安全 管理 責任 者".split(" ")]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sudachi_mode_b(self):
        """Test Sudachi tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="Sudachi",
                mode="B",
            )
        except ModuleNotFoundError:
            pytest.skip("skip sudachi")

        expect = [Token(surface=w) for w in "医薬品 安全 管理 責任者".split(" ")]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sudachi_mode_c(self):
        """Test Sudachi tokenizer."""
        try:
            tokenizer = WordTokenizer(
                tokenizer="Sudachi",
                mode="C",
            )
        except ModuleNotFoundError:
            pytest.skip("skip sudachi")

        expect = [Token(surface=w) for w in "医薬品安全管理責任者".split(" ")]
        result = tokenizer.tokenize(SENTENCE2)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_character(self):
        """Test Character tokenizer."""
        tokenizer1 = WordTokenizer(tokenizer="Character")
        tokenizer2 = WordTokenizer(tokenizer="character")
        # assert tokenizer1 == tokenizer2
        expect  = [Token(surface=w) for w in "吾 輩 は 猫 で あ る".split(" ")]  # NOQA
        result1 = tokenizer1.tokenize(SENTENCE1)
        result2 = tokenizer2.tokenize(SENTENCE1)
        assert expect  == result1  # NOQA
        assert result1 == result2
