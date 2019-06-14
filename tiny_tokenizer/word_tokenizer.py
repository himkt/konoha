"""Word Level Tokenizer."""
import warnings


class WordTokenizer:
    """Tokenizer takes a sentence into tokens."""

    def __init__(self, tokenizer=None, flags=''):
        """Create tokenizer.

        Keyword Arguments:
            tokenizer {str or None} -- specify the type of tokenizer (default: {None})  # NOQA
            flags {str} -- option passing to tokenizer (default: {''})
        """
        if tokenizer is None:
            self.tokenize = self.__identity
            self.__tokenizer_name = 'identity'
            warnings.warn('No tokenizer specified. Return input directly')
            return

        __tokenizer = tokenizer.lower()

        if __tokenizer == 'character':
            self.__tokenizer_name = 'Character'
            self.tokenize = self.__character_level_tokenize
            return

        # use external libraries
        if __tokenizer == 'mecab':
            import natto
            flags = '-Owakati' if not flags else flags
            self.__tokenizer = natto.MeCab(flags)
            self.__tokenizer_name = 'MeCab'
            self.tokenize = self.__mecab_tokenize

        if __tokenizer == 'kytea':
            import Mykytea
            self.__tokenizer = Mykytea.Mykytea(flags)
            self.__tokenizer_name = 'KyTea'
            self.tokenize = self.__kytea_tokenize

        elif __tokenizer == 'sentencepiece':
            import sentencepiece
            self.__tokenizer = sentencepiece.SentencePieceProcessor()
            self.__tokenizer.load(flags)
            self.__tokenizer_name = 'Sentencepiece'
            self.tokenize = self.__sentencepiece_tokenize

    def __identity(self, sentence):
        """Return input sentence directly."""
        return sentence

    def __mecab_tokenize(self, sentence):
        """Mecab tokenizer.

        Arguments:
            sentence {str} -- raw sentence
        """
        return self.__tokenizer.parse(sentence)

    def __kytea_tokenize(self, sentence):
        """Kytea tokenizer.

        Arguments:
            sentence {str} -- raw sentence
        """
        return ' '.join(self.__tokenizer.getWS(sentence))

    def __sentencepiece_tokenize(self, sentence):
        """Sentencepiece tokenizer.

        Arguments:
            sentence {str} -- raw sentence
        """
        return ' '.join(self.__tokenizer.EncodeAsPieces(sentence))

    def __character_level_tokenize(self, sentence):
        """Character level tokenizer.

        Arguments:
            sentence {str} -- raw sentence
        """
        return ' '.join(list(sentence))

    @property
    def tokenizer_name(self):
        return self.__tokenizer_name


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
