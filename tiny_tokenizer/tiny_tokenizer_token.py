from typing import Optional


class Token:
    """Token class for tiny_tokenizer."""

    def __init__(
            self,
            surface: str,
            postag: Optional[str] = None,
            postag2: Optional[str] = None
    ):
        """
        Initializer for Token.

        Parameters
        ---
        surface (str)
            surface (original form) of a word
        postag (Optional[str], default None)
            part-of-speech tag of a word (optional)
        postag2 (Optional[str], default None)
            detailed part-of-speech tag of a word (optional)
        """
        self.surface = surface
        self.postag  = postag  # NOQA
        self.postag2 = postag2

    def __repr__(self):
        representation = self.surface
        if self.postag is not None:
            representation += f" ({self.postag})"
        return representation

    def __eq__(self, right):
        return self.surface == right.surface \
            and self.postag == right.postag \
            and self.postag2 == right.postag2
