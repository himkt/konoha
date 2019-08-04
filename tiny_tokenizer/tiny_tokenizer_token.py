from typing import Optional


class Token:
    """Token class."""

    def __init__(self, surface: str, postag: Optional[str] = None):
        """
        Initializer for Token.

        Parameters
        ---
        surface (str)
            surface (original form) of a word
        postag (Optional[str]=None)
            part-of-speech tag of a word (option)
        """
        self.surface = surface
        self.postag = postag

    def __repr__(self):
        representation = self.surface
        if self.postag is not None:
            representation += f" ({self.postag})"
        return representation

    def __eq__(self, right):
        return self.surface == right.surface and self.postag == right.postag
