import warnings


class WordTokenizer:
    def __init__(self, tokenizer=None, flags=''):
        """
        :param tokenizer: specify tokenizer you use
        :type tokenizer: str
        :param flags: tokenizer's flags
        :type flags: str
        :rtype: None
        """
        if tokenizer == 'KyTea':
            import Mykytea
            self.tokenizer = Mykytea.Mykytea(flags)
            self.tokenize = self._kytea_tokenize

        elif tokenizer == 'MeCab':
            import natto
            flags = '-Owakati' if not flags else flags
            self.tokenizer = natto.MeCab(flags)
            self.tokenize = self._mecab_tokenize

        elif tokenizer == 'Sentencepiece':
            import sentencepiece
            self.tokenizer = sentencepiece.SentencePieceProcessor()
            self.tokenizer.load(flags)
            self.tokenize = self._sentencepiece_tokenize

        elif tokenizer == 'Character':
            self.tokenize = self._character_level_tokenizer

        else:
            warnings.warn('Return input directly')
            self.tokenizer = None
            self.tokenize = lambda x: x

    def _mecab_tokenize(self, sentence):
        """
        :param sentence: a sentence to be tokenized
        :type sentence: str
        :return: a tokenized sentence words \
            are segmented with whitespace
        :rtype: str
        """
        return self.tokenizer.parse(sentence)

    def _kytea_tokenize(self, sentence):
        """
        :param sentence: a sentence to be tokenized
        :type sentence: str
        :return: a tokenized sentence words \
            are segmented with whitespace
        :rtype: str
        """
        return ' '.join(self.tokenizer.getWS(sentence))

    def _sentencepiece_tokenize(self, sentence):
        """sentencepiece tokenizer

        Arguments:
            sentence {str} -- raw sentence
        """
        return ' '.join(self.tokenizer.EncodeAsPieces(sentence))

    def _character_level_tokenizer(self, sentence):
        """return a list of characters

        Arguments:
            sentence {str} -- raw sentence
        """
        return ' '.join(list(sentence))


if __name__ == '__main__':
    word_tokenizer = WordTokenizer('KyTea')
    res = word_tokenizer.tokenize('我輩は猫である')
    print(res)

    word_tokenizer = WordTokenizer('MeCab')
    res = word_tokenizer.tokenize('我輩は猫である')
    print(res)

    word_tokenizer = WordTokenizer('Sentencepiece', 'data/model.spm')
    res = word_tokenizer.tokenize('我輩は猫である')
    print(res)

    word_tokenizer = WordTokenizer('Character')
    res = word_tokenizer.tokenize('我輩は猫である')
    print(res)