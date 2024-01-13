from konoha.word_tokenizers.tokenizer import BaseTokenizer


class KonohaAPITokenizer(BaseTokenizer):
    def __init__(self, tokenizer: str):
        super().__init__(name=f"{tokenizer} (remote)")

    def tokenize(self, text: str):
        pass
