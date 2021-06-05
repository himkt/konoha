from konoha import SentenceTokenizer
from konoha import WordTokenizer


if __name__ == "__main__":
    sentence_tokenizer = SentenceTokenizer()
    tokenizers = ["MeCab", "KyTea", "Janome", "nagisa", "Character"]
    tokenizers_support_postag = ["MeCab", "KyTea", "Janome", "nagisa"]

    word_tokenizers = []
    for word_tokenizer_name in tokenizers:
        try:
            _tokenizer = WordTokenizer(word_tokenizer_name)
            word_tokenizers.append(_tokenizer)

            if word_tokenizer_name in tokenizers_support_postag:
                _tokenizer = WordTokenizer(word_tokenizer_name)
                word_tokenizers.append(_tokenizer)

        except (ImportError, RuntimeError):
            print("Skip: ", word_tokenizer_name)

    try:
        _tokenizer = WordTokenizer(
            "Sentencepiece", model_path="./data/model.spm"
        )  # NOQA
        word_tokenizers.append(_tokenizer)

    except (ImportError, OSError, RuntimeError):
        print("Skip: ", "Sentencepiece")

    try:
        _tokenizer = WordTokenizer("Sudachi", mode="A")
        word_tokenizers.append(_tokenizer)

    except (ImportError, KeyError):
        print("Skip: ", "Sudachi")

    print("Finish creating word tokenizers")
    print()

    # ref: https://ja.wikipedia.org/wiki/東京特許許可局
    document = "東京特許許可局（とうきょうとっきょきょかきょく） 日本語の早口言葉。"  # NOQA
    document += "なお実際に特許に関する行政を行うのは特許庁であり、過去にこのような役所が存在したことは一度も無い。"  # NOQA
    print("Given document: {}".format(document))

    sentences = sentence_tokenizer.tokenize(document)
    for sentence_id, sentence in enumerate(sentences):
        print("#{}: {}".format(sentence_id, sentence))

        for word_tokenizer in word_tokenizers:
            print("Tokenizer: {}".format(word_tokenizer.name))
            result = word_tokenizer.tokenize(sentence)
            result = [str(r) for r in result]
            print(" ".join(result))

        print()
