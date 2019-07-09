from tiny_tokenizer import SentenceTokenizer
from tiny_tokenizer import WordTokenizer


if __name__ == "__main__":
    sentence_tokenizer = SentenceTokenizer()
    word_tokenizers = []
    word_tokenizers.append(WordTokenizer())  # return input directly
    word_tokenizers.append(WordTokenizer("MeCab"))
    word_tokenizers.append(WordTokenizer("KyTea"))
    word_tokenizers.append(WordTokenizer("Sentencepiece", "data/model.spm"))
    word_tokenizers.append(WordTokenizer("Character"))
    print("Finish creating word tokenizers")
    print()

    document = "我輩は猫である。名前はまだない"
    print(f"Given document: {document}")

    sentences = sentence_tokenizer.tokenize(document)
    for sentence_id, sentence in enumerate(sentences):
        print(f"#{sentence_id}: {sentence}")

        for tokenizer in word_tokenizers:
            result = tokenizer.tokenize(sentence)
            print(f"Tokenizer ({tokenizer.tokenizer_name}): {result}")

        print()
