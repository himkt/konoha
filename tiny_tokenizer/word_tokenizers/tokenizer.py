

class BaseTokenizer:
    """Base class for word leveltiny_tokenizer.tokenizer"""

    def __init__(self, name: str, with_postag: bool = False, **kwargs):
        """
        Abstract class for word leveltiny_tokenizer.tokenizer.

        Parameters
        ---
        name (str)
            name of atiny_tokenizer.tokenizer
        with_postag (bool=False)
            flag determines iftiny_tokenizer.tokenizer include pos tags.
        **kwargs
            others.
        """
        self.__name = name
        self.with_postag = with_postag

    def tokenize(self, text: str):
        """Abstract method fortiny_tokenizer.tokenization"""
        raise NotImplementedError

    @property
    def name(self):
        """Return name oftiny_tokenizer.tokenizer"""
        return self.__name
