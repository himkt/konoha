from tiny_tokenizer import SentenceTokenizer
from tiny_tokenizer import WordTokenizer


if __name__ == "__main__":
    sentence_tokenizer = SentenceTokenizer()
    tokenizers = ["MeCab", "KyTea", "Character"]
    tokenizers_support_postag = ["MeCab", "KyTea"]

    word_tokenizers = []
    for tokenizer in tokenizers:
        try:
            _tokenizer = WordTokenizer(tokenizer)
            word_tokenizers.append(_tokenizer)

            if tokenizer in tokenizers_support_postag:
                _tokenizer = WordTokenizer(tokenizer, with_postag=True)
                word_tokenizers.append(_tokenizer)

        except ModuleNotFoundError:
            print("Skip: ", tokenizer)

    try:
        _tokenizer = WordTokenizer("Sentencepiece", model_path="./data/model.spm")  # NOQA
        word_tokenizers.append(_tokenizer)

    except ModuleNotFoundError:
        print("Skip: ", "Sentencepiece")

    try:
        _tokenizer = WordTokenizer("Sudachi", mode="A", with_postag=True)
        word_tokenizers.append(_tokenizer)

    except ModuleNotFoundError:
        print("Skip: ", "Sudachi")

    print("Finish creating word tokenizers")
    print()

    document = "我輩は猫である。名前はまだない"
    print(f"Given document: {document}")

    sentences = sentence_tokenizer.tokenize(document)
    for sentence_id, sentence in enumerate(sentences):
        print(f"#{sentence_id}: {sentence}")

        for tokenizer in word_tokenizers:
            print(f"Tokenizer: {tokenizer.name}")
            result = tokenizer.tokenize(sentence)
            result = [str(r) for r in result]
            print(' '.join(result))

        print()
