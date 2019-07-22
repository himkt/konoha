from tiny_tokenizer import SentenceTokenizer
from tiny_tokenizer import WordTokenizer


if __name__ == "__main__":
    sentence_tokenizer = SentenceTokenizer()
    word_tokenizers = []
    word_tokenizers.append(["MeCab", WordTokenizer(tokenizer="MeCab")])
    word_tokenizers.append(["MeCab", WordTokenizer(tokenizer="MeCab", with_postag=True)])  # NOQA
    word_tokenizers.append(["KyTea", WordTokenizer(tokenizer="KyTea")])
    word_tokenizers.append(["KyTea", WordTokenizer(tokenizer="KyTea", with_postag=True)])  # NOQA
    word_tokenizers.append(["Sentencepiece", WordTokenizer(tokenizer="Sentencepiece", model_path="data/model.spm")])  # NOQA
    word_tokenizers.append(["Sudachi (A)", WordTokenizer(tokenizer="Sudachi", mode="A")])  # NOQA
    word_tokenizers.append(["Sudachi (A)", WordTokenizer(tokenizer="Sudachi", with_postag=True, mode="A")])  # NOQA
    word_tokenizers.append(["Sudachi (B)", WordTokenizer(tokenizer="Sudachi", mode="B")])  # NOQA
    word_tokenizers.append(["Sudachi (B)", WordTokenizer(tokenizer="Sudachi", with_postag=True, mode="B")])  # NOQA
    word_tokenizers.append(["Sudachi (C)", WordTokenizer(tokenizer="Sudachi", mode="C")])  # NOQA
    word_tokenizers.append(["Sudachi (C)", WordTokenizer(tokenizer="Sudachi", with_postag=True, mode="C")])  # NOQA
    word_tokenizers.append(["Character", WordTokenizer(tokenizer="Character")])  # NOQA
    print("Finish creating word tokenizers")
    print()

    document = "我輩は猫である。名前はまだない"
    print(f"Given document: {document}")

    sentences = sentence_tokenizer.tokenize(document)
    for sentence_id, sentence in enumerate(sentences):
        print(f"#{sentence_id}: {sentence}")

        for name, tokenizer in word_tokenizers:
            print(f"Tokenizer: {name}")
            result = tokenizer.tokenize(sentence)
            print(result)

        print()
