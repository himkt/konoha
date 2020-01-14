

class BaseTokenizer:
    """Base class for word levelkonoha.tokenizer"""

    def __init__(self, name: str, with_postag: bool = False, **kwargs):
        """
        Abstract class for word levelkonoha.tokenizer.

        Parameters
        ---
        name (str)
            name of akonoha.tokenizer
        with_postag (bool=False)
            flag determines ifkonoha.tokenizer include pos tags.
        **kwargs
            others.
        """
        self.__name = name
        self.with_postag = with_postag

    def tokenize(self, text: str):
        """Abstract method forkonoha.tokenization"""
        raise NotImplementedError

    @property
    def name(self):
        """Return name ofkonoha.tokenizer"""
        return self.__name
