import warnings


class CharacterTokenizer:
    def __init__(self):
        pass

    def tokenize(self, sentence):
        """
        :param sentence: a sentence to be tokenized
        :type sentence: str
        :return: a list of characters
        :type: str
        """
        return list(sentence)


if __name__ == '__main__':
    character_tokenizer = CharacterTokenizer()
    res = character_tokenizer.tokenize('我輩は猫である')
    print(res)
