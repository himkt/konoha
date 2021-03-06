"""__init__.py."""
from konoha.sentence_tokenizer import SentenceTokenizer  # NOQA
from konoha.word_tokenizer import WordTokenizer  # NOQA
from importlib_metadata import version


__version__ = version("konoha")
