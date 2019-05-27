from tiny_tokenizer.character_tokenizer import CharacterTokenizer
import unittest


SENTENCE1 = '吾輩は猫である'


class CharacterTokenizerTest(unittest.TestCase):
    def test_character_tokenize(self):
        tokenizer = CharacterTokenizer()
        expect = ['吾', '輩', 'は', '猫', 'で', 'あ', 'る']
        result = tokenizer.tokenize(SENTENCE1)
        self.assertEqual(expect, result)
