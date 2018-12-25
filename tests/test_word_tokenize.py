from tiny_tokenizer.word_tokenizer import WordTokenizer
import unittest


SENTENCE1 = '吾輩は猫である'


class WordTokenizerTest(unittest.TestCase):
    def test_word_tokenize_with_kytea(self):
        tokenizer = WordTokenizer('KyTea')
        expect = '吾輩 は 猫 で あ る'
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_tokenize_with_mecab(self):
        tokenizer = WordTokenizer('MeCab')
        expect = '吾輩 は 猫 で ある'
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)

    def test_word_without_tokenizer(self):
        tokenizer = WordTokenizer()
        expect = '吾輩は猫である'
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)
