import pytest

from konoha.integrations.allennlp import KonohaTokenizer


def test_allennlp_mecab():
    try:
        import allennlp  # NOQA
        import natto  # NOQA
    except ImportError:
        pytest.skip("AllenNLP or MeCab is not installed.")

    tokenizer = KonohaTokenizer(tokenizer_name='mecab')
    tokens_konoha = tokenizer.tokenize("吾輩は猫である")
    token_surfaces = "吾輩 は 猫 で ある".split()
    assert token_surfaces == list(t.text for t in tokens_konoha)


def test_allennlp_janome():
    try:
        import allennlp  # NOQA
        import janome  # NOQA
    except ImportError:
        pytest.skip("AllenNLP or Janome is not installed.")

    tokenizer = KonohaTokenizer(tokenizer_name='janome')
    tokens_konoha = tokenizer.tokenize("吾輩は猫である")
    token_surfaces = "吾輩 は 猫 で ある".split()
    assert token_surfaces == list(t.text for t in tokens_konoha)


def test_allennlp_kytea():
    try:
        import allennlp  # NOQA
        import Mykytea  # NOQA
    except ImportError:
        pytest.skip("AllenNLP or KyTea is not installed.")
    tokenizer = KonohaTokenizer(tokenizer_name='kytea')
    tokens_konoha = tokenizer.tokenize("吾輩は猫である")
    token_surfaces = "吾輩 は 猫 で あ る".split()
    assert token_surfaces == list(t.text for t in tokens_konoha)


def test_allennlp_sentencepiece():
    try:
        import allennlp  # NOQA
        import sentencepiece  # NOQA
    except ImportError:
        pytest.skip("AllenNLP or Sentencepiece is not installed.")
    tokenizer = KonohaTokenizer(
        tokenizer_name='sentencepiece',
        model_path="data/model.spm"
    )
    tokens_konoha = tokenizer.tokenize("吾輩は猫である")
    token_surfaces = "▁ 吾 輩 は 猫 である".split()
    assert token_surfaces == list(t.text for t in tokens_konoha)


def test_allennlp_sudachi():
    try:
        import allennlp  # NOQA
        import sudachipy  # NOQA
    except ImportError:
        pytest.skip("AllenNLP or SudachiPy is not installed.")
    tokenizer = KonohaTokenizer(
        tokenizer_name='sudachi',
        mode="A",
    )
    tokens_konoha = tokenizer.tokenize("医薬品安全管理責任者")
    token_surfaces = "医薬 品 安全 管理 責任 者".split()
    assert token_surfaces == list(t.text for t in tokens_konoha)
