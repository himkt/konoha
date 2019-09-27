"""setup.py."""

from os import getenv

from setuptools import find_packages
from setuptools import setup


try:
    BUILD_WORD_TOKENIZER = int(getenv("BUILD_WORD_TOKENIZER", '1'))
except ValueError:
    raise ValueError("BUILD_WORD_TOKENIZER should be integer")

setup(
    name="tiny_tokenizer",
    version="3.0.1",
    description="Tiny Word/Sentence Tokenizer",
    author="himkt",
    author_email="himkt@klis.tsukuba.ac.jp",
    extras_require={
        "mecab": ["natto-py"],
        "kytea": ["kytea"],
        "sentencepiece": ["sentencepiece"],
        "sudachi": ["SudachiPy"],
        "all": ["natto-py", "kytea", "sentencepiece", "SudachiPy"]
    },
    url="https://github.com/himkt/tiny_tokenizer",
    packages=find_packages(),
)
