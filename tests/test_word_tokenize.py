from tiny_tokenizer.word_tokenizer import WordTokenizer

import unittest
import pytest


SENTENCE1 = "吾輩は猫である"


class WordTokenizerTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="KyTea")
        except ModuleNotFoundError:
            pytest.skip("skip kytea")

        expect = "吾輩 は 猫 で あ る".split(" ")
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="MeCab")
        except ModuleNotFoundError:
            pytest.skip("skip mecab")

        expect = "吾輩 は 猫 で ある".split(" ")
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

        expect = "▁ 吾 輩 は 猫 である".split(" ")
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_character(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer(
            tokenizer="Character"
        )
        expect = "吾 輩 は 猫 で あ る".split(" ")
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)


class WordTokenizerWithLowerCaseTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="kytea")
        except ModuleNotFoundError:
            pytest.skip("skip kytea")

        expect = "吾輩 は 猫 で あ る".split(" ")
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        try:
            tokenizer = WordTokenizer(tokenizer="mecab")
        except ModuleNotFoundError:
            pytest.skip("skip mecab")

        expect = "吾輩 は 猫 で ある".split(" ")
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

        expect = "▁ 吾 輩 は 猫 である".split(" ")
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_character(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer(tokenizer="character")
        expect = "吾 輩 は 猫 で あ る".split(" ")
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)
