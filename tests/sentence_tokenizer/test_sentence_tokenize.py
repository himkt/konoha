from konoha.sentence_tokenizer import SentenceTokenizer

DOCUMENT1 = """
私は猫である。にゃお。\r\n
にゃにゃ

わんわん。にゃーにゃー。
"""

DOCUMENT2 = """
私は猫である（ただしかわいいものとする。異議は認める）。にゃお。\r\n
にゃにゃ
"""

DOCUMENT3 = """
猫「にゃおにゃ。ただしかわいいものとする。異議は認める」。

にゃお。にゃにゃ
"""

DOCUMENT4 = """
わんわん。「にゃ？」(にゃー）わんわん。「わおーん。」（犬より。）
"""


def test_sentence_tokenize():
    corpus = SentenceTokenizer()
    expect = ["私は猫である。", "にゃお。", "にゃにゃ", "わんわん。", "にゃーにゃー。"]
    result = corpus.tokenize(DOCUMENT1)
    assert expect == result


def test_sentence_tokenize_with_bracket():
    corpus = SentenceTokenizer()
    expect = ["私は猫である（ただしかわいいものとする。異議は認める）。", "にゃお。", "にゃにゃ"]
    result = corpus.tokenize(DOCUMENT2)
    assert expect == result


def test_sentence_tokenize_with_quotation():
    corpus = SentenceTokenizer()
    expect = ["猫「にゃおにゃ。ただしかわいいものとする。異議は認める」。", "にゃお。", "にゃにゃ"]
    result = corpus.tokenize(DOCUMENT3)
    assert expect == result


def test_sentence_tokenize_with_combined():
    corpus = SentenceTokenizer()
    expect = ["わんわん。", "「にゃ？」(にゃー）わんわん。", "「わおーん。」（犬より。）"]
    result = corpus.tokenize(DOCUMENT4)
    assert expect == result
