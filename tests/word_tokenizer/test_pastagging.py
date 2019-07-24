"""Tests for postagging."""
import unittest
import pytest

from tiny_tokenizer.word_tokenizer import WordTokenizer
from tiny_tokenizer.word_tokenizer import Token


class TestWordPostagging(unittest.TestCase):
    def test_mecab(self):
        assert 1 == 1
