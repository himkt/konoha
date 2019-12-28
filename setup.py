"""setup.py."""

from os import getenv

from setuptools import find_packages
from setuptools import setup


SUDACHIDICT_URL = (
    "https://object-storage.tyo2.conoha.io/v1/"
    "nc_2520839e1f9641b08211a5c85243124a/"
    "sudachi/SudachiDict_core-20190927.tar.gz"
)
SUDACHIDICT = "SudachiDict_core @ {}".format(SUDACHIDICT_URL)

setup(
    name="tiny_tokenizer",
    version="3.1.0",
    description="Tiny Word/Sentence Tokenizer",
    author="himkt",
    author_email="himkt@klis.tsukuba.ac.jp",
    extras_require={
        "mecab": ["natto-py"],
        "kytea": ["kytea"],
        "sentencepiece": ["sentencepiece"],
        "sudachi": ["SudachiPy", SUDACHIDICT],
        "janome": ["janome"],
        "all": ["natto-py", "kytea", "janome", "sentencepiece", "SudachiPy", SUDACHIDICT],
    },
    url="https://github.com/himkt/tiny_tokenizer",
    packages=find_packages(),
)
