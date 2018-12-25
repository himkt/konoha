#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages


setup(name='tiny_tokenizer',
      version='1.0.4',
      description='Tiny Word/Sentence Tokenizer',
      author='himkt',
      author_email='himkt@klis.tsukuba.ac.jp',
      install_requires=['natto-py', 'kytea'],
      url='https://github.com/himkt/tiny_tokenizer',
      packages=find_packages())
