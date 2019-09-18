"""Token class."""
from typing import Optional


class Token:
    """Token class for tiny_tokenizer."""

    def __init__(
        self,
        surface: str,
        postag: Optional[str] = None,
        postag1: Optional[str] = None,
        postag2: Optional[str] = None,
        postag3: Optional[str] = None,
        inflection: Optional[str] = None,
        conjugation: Optional[str] = None,
        original_form: Optional[str] = None,
        yomi: Optional[str] = None,
        pron: Optional[str] = None,
        normalized_form: Optional[str] = None,
    ):
        """
        Initializer for Token.

        Parameters
        ---
        surface (str)
            surface (original form) of a word
        postag (str, default: None)
            part-of-speech tag of a word (optional)
        postag1 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        postag2 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        postag3 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        inflection (str, default: None)
            conjugate type of word (optional)
        conjugation (str, default: None)
            conjugate type of word (optional)
        original_form (str, default: None)
            original form of a word
        yomi (str, default: None)
            yomi of a word (optional)
        pron (str, default: None)
            pronounciation of a word (optional)
        normalized_form (str, default: None)
            normalized form of a word (optional)
            Note that normalized_form is only
            available on SudachiPy
        """
        self.surface = surface
        self.postag = postag
        self.postag1 = postag1
        self.postag2 = postag2
        self.postag3 = postag3
        self.inflection = inflection
        self.conjugation = conjugation
        self.original_form = original_form
        self.pron = pron
        self.yomi = yomi
        self.normalized_form = normalized_form

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
        if self.postag1 is not None:
            feature.append(self.postag1)
        if self.postag2 is not None:
            feature.append(self.postag2)
        if self.postag3 is not None:
            feature.append(self.postag3)
        if self.inflection is not None:
            feature.append(self.inflection)
        if self.conjugation is not None:
            feature.append(self.conjugation)
        if self.original_form is not None:
            feature.append(self.original_form)
        if self.yomi is not None:
            feature.append(self.yomi)
        if self.pron is not None:
            feature.append(self.pron)
        if self.normalized_form is not None:
            feature.append(self.normalized_form)
        return ','.join(feature)
