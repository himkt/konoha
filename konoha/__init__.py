"""__init__.py."""
from importlib_metadata import version

from konoha.sentence_tokenizer import SentenceTokenizer  # NOQA
from konoha.word_tokenizer import WordTokenizer  # NOQA

__version__ = version("konoha")
