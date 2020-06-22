
class Token:
    ...


class Tokenizer:
    def register(func):
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    def batch_tokenize(self, texts):
        raise NotImplementedError

    def tokenize(self, text):
        raise NotImplementedError
