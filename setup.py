"""setup.py."""


from setuptools import find_packages
from setuptools import setup


setup(name='tiny_tokenizer',
      version='1.2.1',
      description='Tiny Word/Sentence Tokenizer',
      author='himkt',
      author_email='himkt@klis.tsukuba.ac.jp',
      install_requires=['natto-py', 'kytea', 'sentencepiece'],
      url='https://github.com/himkt/tiny_tokenizer',
      packages=find_packages())
