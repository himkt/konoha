from tiny_tokenizer.word_tokenizer import WordTokenizer
import unittest


SENTENCE1 = '吾輩は猫である'


class WordTokenizerTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        tokenizer = WordTokenizer('KyTea')
        expect = '吾輩 は 猫 で あ る'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        tokenizer = WordTokenizer('MeCab')
        expect = '吾輩 は 猫 で ある'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sentencepiece(self):
        """Test Sentencepiece tokenizer."""
        tokenizer = WordTokenizer('Sentencepiece', 'data/model.spm')
        expect = '▁ 吾 輩 は 猫 である'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_character(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer('Character')
        expect = '吾 輩 は 猫 で あ る'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_without_tokenizer(self):
        """Test identity tokenizer."""
        tokenizer = WordTokenizer()
        expect = '吾輩は猫である'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)


class WordTokenizerWithLowerCaseTest(unittest.TestCase):
    """Test ordinal word tokenizer."""

    def test_word_tokenize_with_kytea(self):
        """Test KyTea tokenizer."""
        tokenizer = WordTokenizer('kytea')
        expect = '吾輩 は 猫 で あ る'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_mecab(self):
        """Test MeCab tokenizer."""
        tokenizer = WordTokenizer('mecab')
        expect = '吾輩 は 猫 で ある'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_sentencepiece(self):
        """Test Sentencepiece tokenizer."""
        tokenizer = WordTokenizer('sentencepiece', 'data/model.spm')
        expect = '▁ 吾 輩 は 猫 である'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_character(self):
        """Test Character tokenizer."""
        tokenizer = WordTokenizer('character')
        expect = '吾 輩 は 猫 で あ る'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_without_tokenizer(self):
        """Test identity tokenizer."""
        tokenizer = WordTokenizer()
        expect = '吾輩は猫である'.split(' ')
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)
