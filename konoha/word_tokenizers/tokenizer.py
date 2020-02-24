from typing import List
from typing import Dict
from typing import Union
from typing import cast


TokenizerTransformInput = Union[str, List[str]]
TokenizerITransformInput = Union[List[int], List[List[int]]]


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
        self._vocabulary = []  # type: List[str]
        self._word2idx = {}  # type: Dict[str, int]
        self._word2frq = {}  # type: Dict[str, int]
        self.with_postag = with_postag

    def fit_transform(
            self,
            texts: List[str],
            min_tf: int = 0,
            max_tf: int = 1001001001
    ):
        self.fit(texts, min_tf=min_tf, max_tf=max_tf)
        return self.transform(texts)

    def fit(
            self,
            texts: List[str],
            min_tf: int = 0,
            max_tf: int = 1001001001
    ):
        for item in texts:
            for word in self.tokenize(item):
                surface = word.surface
                self._word2frq[surface] = self._word2frq.get(surface, 0) + 1

        self._word2idx = {
            w: i for i, w in enumerate(self._word2frq.keys())
            if min_tf <= self._word2frq[w] <= max_tf
        }
        self._idx2word = {i: w for w, i in self._word2idx.items()}
        self._vocabulary = list(self._word2idx.keys())

    def transform(self, texts: TokenizerTransformInput):
        if isinstance(texts, str):
            texts = [texts]

        sentences = []
        for item in texts:
            sentence = [t.surface for t in self.tokenize(item)]
            sentence = [self._word2idx.get(w, -1) for w in sentence]
            sentences.append(sentence)
        return sentences

    def itransform(self, texts: TokenizerITransformInput):
        if len(texts) == 0:
            return []

        fitst_order = False
        if isinstance(texts[0], int):  # List[int]
            texts = cast(List[List[int]], [texts])
            fitst_order = True
        else:  # List[List[int]]
            texts = cast(List[List[int]], texts)

        isentences = []  # type: List[List[str]]
        for sentence in texts:
            isentence = [self._idx2word.get(i, '<UNK>') for i in sentence]
            isentences.append(isentence)

        if fitst_order:
            return isentences[0]
        return isentences

    def tokenize(self, text: str):
        """Abstract method forkonoha.tokenization"""
        raise NotImplementedError

    @property
    def vocabulary(self):
        return self._vocabulary

    @property
    def name(self):
        """Return name ofkonoha.tokenizer"""
        return self.__name
