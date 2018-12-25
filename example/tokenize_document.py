from tiny_tokenizer import SentenceTokenizer
from tiny_tokenizer import WordTokenizer


if __name__ == '__main__':
    sentence_tokenizer = SentenceTokenizer()
    word_tokenizer_mecab = WordTokenizer('MeCab')
    word_tokenizer_kytea = WordTokenizer('KyTea')
    document = '我輩は猫である。名前はまだない'

    for sentence in sentence_tokenizer.tokenize(document):
        print(sentence)
        print('words: MeCab')
        for word in word_tokenizer_mecab.tokenize(sentence).split(' '):
            print('  ' + word)

        print('words: KyTea')
        for word in word_tokenizer_kytea.tokenize(sentence).split(' '):
            print('  ' + word)
