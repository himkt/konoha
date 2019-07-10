"""Word Level Tokenizer."""
from typing import Optional

import warnings


class Token:
    """Token class"""
    def __init__(
        self,
        surface: str,
        postag: Optional[str] = None
    ):
        self.surface = surface
        self.postag = postag

    def __repr__(self):
        representation = self.surface
        if self.postag is not None:
            representation += f' ({self.postag})'
        return representation

    def __eq__(self, right):
        return self.surface == right.surface and \
            self.postag == right.postag


class BaseWordLevelTokenizer:
    """Base class for word level tokenizer"""
    def __init__(
            self,
            name: str,
            with_postag: bool = False,
            **kwargs,
    ):
        self.__name = name
        self.with_postag = with_postag

    def tokenize(self, text: str):
        """Abstract method for tokenization"""
        raise NotImplementedError

    @property
    def name(self):
        """Return name of tokenizer"""
        return self.__name


class MeCabTokenizer(BaseWordLevelTokenizer):
    """Wrapper class of external text analyzers"""
    def __init__(
        self,
        dictionary_path: Optional[str] = None,
        with_postag: bool = False,
    ):
        super().__init__(name='mecab', with_postag=with_postag)
        try:
            import natto
        except ModuleNotFoundError:
            raise ModuleNotFoundError("natto-py is not installed")

        flag = ''
        if not self.with_postag:
            flag += ' -Owakati'

        if dictionary_path is not None:
            flag += f' -u {dictionary_path}'

        self.mecab = natto.MeCab(flag)

    def tokenize(self, text: str):
        """Tokenize"""
        return_result = []
        parse_result = self.mecab.parse(text)
        if self.with_postag:
            for elem in parse_result.split('\n')[:-1]:
                surface, feature = elem.split()
                postag = feature.split(',')[0]
                return_result.append(Token(surface=surface, postag=postag))
        else:
            for surface in parse_result.split(' '):
                return_result.append(Token(surface=surface))

        return return_result


class KyTeaTokenizer(BaseWordLevelTokenizer):
    """Wrapper class of KyTea"""
    def __init__(
        self,
        with_postag: bool = False,
        **kwargs,
    ):
        super(KyTeaTokenizer, self).__init__(
            name='kytea',
            with_postag=with_postag
        )
        try:
            import Mykytea
        except ModuleNotFoundError:
            raise ModuleNotFoundError("kytea is not installed")

        flag = ''
        self.kytea = Mykytea.Mykytea(flag)

    def tokenize(self, text: str):
        return_result = []

        if self.with_postag:
            for elem in self.kytea.getTagsToString(text).split(' ')[:-1]:
                surface, postag, _ = elem.split('/')
                return_result.append(Token(surface=surface, postag=postag))

        else:
            for surface in list(self.kytea.getWS(text)):
                return_result.append(Token(surface=surface))

        return return_result


class SentencepieceTokenizer(BaseWordLevelTokenizer):
    """Wrapper class of Sentencepiece"""
    def __init__(
        self,
        model_path: str,
        **kwargs,
    ):
        super(SentencepieceTokenizer, self).__init__('sentencepiece')
        try:
            import sentencepiece
        except ModuleNotFoundError:
            raise ModuleNotFoundError("sentencepiece is not installed")

        self.tokenizer = sentencepiece.SentencePieceProcessor()
        self.tokenizer.load(model_path)

    def tokenize(self, text: str):
        return [Token(surface=subword) for subword in
                self.tokenizer.EncodeAsPieces(text)]


class CharacterTokenizer(BaseWordLevelTokenizer):
    """Character tokenizer"""
    def __init__(self):
        super(CharacterTokenizer, self).__init__('character')

    def tokenize(self, text: str):
        return [Token(surface=char) for char in list(text)]


class WordTokenizer:
    """Tokenizer takes a sentence into tokens."""

    def __init__(
        self,
        tokenizer: Optional[str] = None,
        with_postag: bool = False,
        dictionary_path: Optional[str] = None,
        model_path: Optional[str] = None,
    ):
        """Create tokenizer.

        Keyword Arguments:
            tokenizer {str or None} -- specify the type of tokenizer (default: {None})  # NOQA
            flags {str} -- option passing to tokenizer (default: {''})
        """
        self.__tokenizer_name = tokenizer.lower()
        self.with_postag = with_postag
        self.dictionary_path = dictionary_path
        self.model_path = model_path

        self.__setup_tokenizer()

    def __setup_tokenizer(self):
        if self.__tokenizer_name == 'mecab':
            self.tokenizer = MeCabTokenizer(
                dictionary_path=self.dictionary_path,
                with_postag=self.with_postag,
            )
        if self.__tokenizer_name == 'kytea':
            self.tokenizer = KyTeaTokenizer(
                with_postag=self.with_postag
            )
        if self.__tokenizer_name == 'sentencepiece':
            self.tokenizer = SentencepieceTokenizer(
                model_path=self.model_path
            )
        if self.__tokenizer_name == 'character':
            self.tokenizer = CharacterTokenizer()

    def tokenize(self, text: str):
        """Tokenize input text"""
        return self.tokenizer.tokenize(text)

    @property
    def name(self):
        return self.__tokenizer_name


if __name__ == "__main__":
    tokenizer = WordTokenizer(tokenizer='mecab', with_postag=False)
    print(tokenizer.tokenize('我輩は猫である'))

    tokenizer = WordTokenizer(tokenizer='mecab', with_postag=True)
    print(tokenizer.tokenize('我輩は猫である'))

    tokenizer = WordTokenizer("kytea", with_postag=False)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("kytea", with_postag=True)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("sentencepiece", model_path="./data/model.spm")
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("character")
    print(tokenizer.tokenize("我輩は猫である"))
