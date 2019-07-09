"""setup.py."""


from setuptools import find_packages
from setuptools import setup

from os import getenv


try:
    BUILD_WORD_TOKENIZER = int(getenv('BUILD_WORD_TOKENIZER', 1))
except:
    raise ValueError('BUILD_WORD_TOKENIZER should be integer')


install_requires = []
if BUILD_WORD_TOKENIZER == 1:
    install_requires.extend(['natto-py', 'kytea', 'sentencepiece'])
else:
    print('Install sentence tokenizer only')


setup(
    name='tiny_tokenizer',
    version='1.3.1',
    description='Tiny Word/Sentence Tokenizer',
    author='himkt',
    author_email='himkt@klis.tsukuba.ac.jp',
    install_requires=install_requires,
    url='https://github.com/himkt/tiny_tokenizer',
    packages=find_packages()
)
