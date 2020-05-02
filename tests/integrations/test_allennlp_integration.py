from konoha.integrations.allennlp import KonohaTokenizer


def test_konoha_tokenizer():
    tokenizer = KonohaTokenizer()
    tokens_konoha = tokenizer.tokenize("吾輩は猫である")
    token_surfaces = ["吾輩", "は", "猫", "で", "ある"]

    assert token_surfaces == list(t.text for t in tokens_konoha)
