from tiny_tokenizer import SentenceTokenizer
from tiny_tokenizer import WordTokenizer


if __name__ == "__main__":
    sentence_tokenizer = SentenceTokenizer()
    word_tokenizers = []
    word_tokenizers.append(WordTokenizer(tokenizer="MeCab"))
    word_tokenizers.append(WordTokenizer(tokenizer="MeCab", with_postag=True))
    word_tokenizers.append(WordTokenizer(tokenizer="KyTea"))
    word_tokenizers.append(WordTokenizer(tokenizer="KyTea", with_postag=True))
    word_tokenizers.append(WordTokenizer(tokenizer="Sentencepiece", model_path="data/model.spm"))  # NOQA
    word_tokenizers.append(WordTokenizer(tokenizer="Character"))
    print("Finish creating word tokenizers")
    print()

    document = "我輩は猫である。名前はまだない"
    print(f"Given document: {document}")

    sentences = sentence_tokenizer.tokenize(document)
    for sentence_id, sentence in enumerate(sentences):
        print(f"#{sentence_id}: {sentence}")

        for tokenizer in word_tokenizers:
            result = tokenizer.tokenize(sentence)
            print(f"Tokenizer ({tokenizer.name}): {result}")

        print()
