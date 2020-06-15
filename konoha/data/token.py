"""Token class."""
from typing import Optional


class Token:
    """Token class for konoha."""

    def __init__(
        self,
        surface: str,
        postag: Optional[str] = None,
        postag2: Optional[str] = None,
        postag3: Optional[str] = None,
        postag4: Optional[str] = None,
        inflection: Optional[str] = None,
        conjugation: Optional[str] = None,
        base_form: Optional[str] = None,
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
        postag2 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        postag3 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        postag4 (str, default: None)
            detailed part-of-speech tag of a word (optional)
        inflection (str, default: None)
            conjugate type of word (optional)
        conjugation (str, default: None)
            conjugate type of word (optional)
        base_form (str, default: None)
            base form of a word
        yomi (str, default: None)
            yomi of a word (optional)
        pron (str, default: None)
            pronounciation of a word (optional)
        normalized_form (str, default: None)
            normalized form of a word (optional)
            Note that normalized_form is only
            available on SudachiPy
        """
        self._surface = surface
        self._postag = postag
        self._postag2 = postag2
        self._postag3 = postag3
        self._postag4 = postag4
        self._inflection = inflection
        self._conjugation = conjugation
        self._base_form = base_form
        self._yomi = yomi
        self._pron = pron
        self._normalized_form = normalized_form

    def __repr__(self) -> str:
        representation = self._surface
        if self._postag is not None:
            representation += " ({})".format(self._postag)
        return representation

    def __eq__(self, right) -> bool:
        return (
            self._surface == right.surface
            and self._postag == right.postag
            and self._postag3 == right.postag3
            and self._yomi == right.yomi
        )

    @property
    def surface(self):
        return self._surface

    @property
    def postag(self):
        return self._postag

    @property
    def postag2(self):
        return self._postag2

    @property
    def postag3(self):
        return self._postag3

    @property
    def postag4(self):
        return self._postag4

    @property
    def inflection(self):
        return self._inflection

    @property
    def conjugation(self):
        return self._conjugation

    @property
    def base_form(self):
        return self._base_form

    @property
    def yomi(self):
        return self._yomi

    @property
    def pron(self):
        return self._pron

    @property
    def normalized_form(self):
        return self._normalized_form

    @property
    def feature(self) -> str:
        feature = []
        if self.postag is not None:
            feature.append(self.postag)
        if self.postag2 is not None:
            feature.append(self.postag2)
        if self.postag3 is not None:
            feature.append(self.postag3)
        if self.postag4 is not None:
            feature.append(self.postag4)
        if self.inflection is not None:
            feature.append(self.inflection)
        if self.conjugation is not None:
            feature.append(self.conjugation)
        if self.base_form is not None:
            feature.append(self.base_form)
        if self.yomi is not None:
            feature.append(self.yomi)
        if self.pron is not None:
            feature.append(self.pron)
        if self.normalized_form is not None:
            feature.append(self.normalized_form)
        return ",".join(feature)
