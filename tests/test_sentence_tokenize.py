from src.sentence_tokenizer import SentenceTokenizer
import unittest


DOCUMENT1 = '''
私は猫である。にゃお。\r\n
にゃにゃ

わんわん。にゃーにゃー。
'''

DOCUMENT2 = '''
私は猫である（ただしかわいいものとする。異議は認める）。にゃお。\r\n
にゃにゃ
'''


class TestSentenceTokenizer(unittest.TestCase):
    def test_sentence_tokenize(self):
        corpus = SentenceTokenizer()
        expect = ['私は猫である。', 'にゃお。', 'にゃにゃ', 'わんわん。', 'にゃーにゃー。']
        result = corpus.tokenize(DOCUMENT1)
        self.assertEqual(expect, result)

    def test_sentence_tokenize_with_bracket(self):
        corpus = SentenceTokenizer()
        expect = ['私は猫である（ただしかわいいものとする。異議は認める）。', 'にゃお。', 'にゃにゃ']
        result = corpus.tokenize(DOCUMENT2)
        self.assertEqual(expect, result)
