"""Token class."""
from typing import Optional


class Token:
    """Token class for tiny_tokenizer."""

    def __init__(
        self,
        surface: str,
        postag: Optional[str] = None,
        postag2: Optional[str] = None,
        conj_type: Optional[str] = None,
        conj_form: Optional[str] = None,
        origin_form: Optional[str] = None,
        yomi: Optional[str] = None,
        pron: Optional[str] = None,
    ):
        """
        Initializer for Token.

        Parameters
        ---
        surface (str)
            surface (original form) of a word
        postag (str, default: None)
            part-of-speech tag of a word (optional)
        postag2 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        conjugate type (str, default: None)
            conjugate type of word (optional)
        conjugate form (str, default: None)
            conjugate type of word (optional)
        origin_form (str, default: None)
            original form of a word
        yomi (str, default: None)
            yomi of a word (optional)
        pron (str, default: None)
            pronounciation of a word (optional)
        """
        self.surface = surface
        self.postag = postag
        self.postag2 = postag2
        self.conj_type = conj_type
        self.conj_form = conj_form
        self.origin_form = origin_form
        self.pron = pron
        self.yomi = yomi

    def __repr__(self):
        representation = self.surface
        if self.postag is not None:
            representation += f" ({self.postag})"
        return representation

    def __eq__(self, right):
        return (
            self.surface == right.surface
            and self.postag == right.postag
            and self.postag2 == right.postag2
            and self.yomi == right.yomi)

    @property
    def feature(self):
        feature = []
        if self.postag is not None:
            feature.append(self.postag)
        if self.postag2 is not None:
            feature.append(self.postag2)
        if self.conj_type is not None:
            feature.append(self.conj_type)
        if self.conj_form is not None:
            feature.append(self.conj_form)
        if self.origin_form is not None:
            feature.append(self.origin_form)
        if self.yomi is not None:
            feature.append(self.yomi)
        if self.pron is not None:
            feature.append(self.pron)
        return ','.join(feature)
