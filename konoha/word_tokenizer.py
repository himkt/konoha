"""Word Level Tokenizer."""
from typing import Optional

from konoha import word_tokenizers
from konoha import resource


class WordTokenizer:
    """Tokenizer takes a sentence into tokens."""

    def __init__(
        self,
        tokenizer: str = 'MeCab',
        with_postag: bool = False,
        user_dictionary_path: Optional[str] = None,
        system_dictionary_path: Optional[str] = None,
        model_path: Optional[str] = None,
        mode: Optional[str] = None,
    ):
        """Create tokenizer.

        Keyword Arguments:
            tokenizer {str or None} -- specify the type of tokenizer (default: {None})  # NOQA
            flags {str} -- option passing to tokenizer (default: {''})
        """
        user_dictionary = resource.Resource(user_dictionary_path)
        system_dictionary = resource.Resource(system_dictionary_path)
        model = resource.Resource(model_path)

        self._tokenizer = tokenizer.lower()
        self.with_postag = with_postag
        self.user_dictionary_path = user_dictionary.path
        self.system_dictionary_path = system_dictionary.path
        self.model_path = model.path

        if mode is not None:
            self.mode = mode.lower()

        self.__setup_tokenizer()

    def __setup_tokenizer(self):
        if self._tokenizer == "character":
            self.tokenizer = word_tokenizers.CharacterTokenizer()

        if self._tokenizer == "whitespace":
            self.tokenizer = word_tokenizers.WhitespaceTokenizer()

        if self._tokenizer == "kytea":
            self.tokenizer = word_tokenizers.KyTeaTokenizer(
                with_postag=self.with_postag,
                model_path=self.model_path
            )

        if self._tokenizer == "sentencepiece":
            self.tokenizer = word_tokenizers.SentencepieceTokenizer(
                model_path=self.model_path
            )

        if self._tokenizer == "mecab":
            self.tokenizer = word_tokenizers.MeCabTokenizer(
                user_dictionary_path=self.user_dictionary_path,
                system_dictionary_path=self.system_dictionary_path,
                with_postag=self.with_postag,
            )

        if self._tokenizer == "janome":
            self.tokenizer = word_tokenizers.JanomeTokenizer(
                user_dictionary_path=self.user_dictionary_path,
                with_postag=self.with_postag
            )

        if self._tokenizer == "sudachi":
            self.tokenizer = word_tokenizers.SudachiTokenizer(
                mode=self.mode,
                with_postag=self.with_postag
            )

    def tokenize(self, text: str):
        """Tokenize input text"""
        return self.tokenizer.tokenize(text)

    @property
    def name(self):
        return self.tokenizer.name


if __name__ == "__main__":
    tokenizer = WordTokenizer(tokenizer="mecab", with_postag=False)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer(tokenizer="mecab", with_postag=True)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("kytea", with_postag=False)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("kytea", with_postag=True)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("janome", with_postag=True)
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("sentencepiece", model_path="./data/model.spm")
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("sudachi", mode="A")
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("character")
    print(tokenizer.tokenize("我輩は猫である"))

    tokenizer = WordTokenizer("whitespace")
    print(tokenizer.tokenize("我輩 は 猫 で ある"))
