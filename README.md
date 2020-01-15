# konoha

(previous tiny_tokenizer)

![Build Status](https://github.com/himkt/konoha/workflows/Python%20package/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/himkt/konoha.svg?maxAge=2592000&colorB=blue)](https://github.com/himkt/konoha/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/himkt/konoha.svg)](https://github.com/himkt/konoha/issues)
[![GitHub release](https://img.shields.io/github/release/himkt/konoha.svg?maxAge=2592000&colorB=red)](https://github.com/himkt/konoha)
[![MIT License](http://img.shields.io/badge/license-MIT-yellow.svg?style=flat)](LICENSE)


## Requirements

- Python>=3.5.0
- pip>=19.0


## Introduction

`konoha` is a simple wrapper of wrapper for Japanese tokenizers.

It unifies the interface of several Japanese tokenizers.

`konoha` provides you the way to switch a tokenizer and boost your pre-processing.

`konoha` supports following tokenizers.
- MeCab (and [natto-py](https://github.com/buruzaemon/natto-py))
- KyTea (and [Mykytea-python](https://github.com/chezou/Mykytea-python))
- Sudachi ([SudachiPy](https://github.com/WorksApplications/SudachiPy))
- Sentencepiece ([Sentencepiece](https://github.com/google/sentencepiece))
- character-based
- whitespace-based

Also, `konoha` provides a simple rule-based sentence tokenizer,
which segments a document into sentences.


## Installation

### Install konoha on local machine

It is not needed for sentence level tokenization because these libraries are used in word level tokenization.

You can install konoha and above libraries by pip, please run:
`pip install konoha[all]`.

Or, you can install konoha only with SentenceTokenizer by the following command:
`pip install konoha`.

**Note**

If you want to use SudachiPy, please run `pip install https://object-storage.tyo2.conoha.io/v1/nc_2520839e1f9641b08211a5c85243124a/sudachi/SudachiDict_core-20191224.tar.gz` to install a dictionary.

### Install konoha on Docker container

You can use konoha using the Docker container.

If you want to use konoha with Docker, run following commands.

```
docker build -t himkt/konoha .
docker run -it himkt/konoha /bin/bash
```


## Example

### Word level tokenization

- Code

```python
from konoha import WordTokenizer

sentence = '自然言語処理を勉強しています'

tokenizer = WordTokenizer('MeCab')
print(tokenizer.tokenize())

tokenizer = WordTokenizer('Sentencepiece', model_path="data/model.spm")
print(tokenizer.tokenize(sentence))
```

- Output

```
[自然, 言語, 処理, を, 勉強, し, て, い, ます]
[▁, 自然, 言語, 処理, を, 勉強, し, ています]
```

For more detail, please see the `example/` directory.

### Sentence level tokenization

- Code

```python
from konoha import SentenceTokenizer

sentence = "私は猫だ。名前なんてものはない。だが，「かわいい。それで十分だろう」。"

tokenizer = SentenceTokenizer()
print(tokenizer.tokenize(sentence))
```

- Output

```
['私は猫だ。', '名前なんてものはない。', 'だが，「かわいい。それで十分だろう」。']
```


### Remote files

konoha can load a dictionary/model on a remote location (it currently supports amazon s3).
For using the remote feature, please run `pip install konoha[remote]` or `pip install konoha[all]`.

```python
from konoha import WordTokenizer

if __name__ == "__main__":
    sentence = "首都大学東京"

    word_tokenizer = WordTokenizer("mecab")
    print(word_tokenizer.tokenize(sentence))

    word_tokenizer = WordTokenizer("mecab", user_dictionary_path="s3://abc/xxx.dic")
    print(word_tokenizer.tokenize(sentence))

    word_tokenizer = WordTokenizer("mecab", system_dictionary_path="s3://abc/yyy")
    print(word_tokenizer.tokenize(sentence))

    word_tokenizer = WordTokenizer("sentencepiece", model_path="s3://abc/zzz.model")
    print(word_tokenizer.tokenize(sentence))
```


## Test

```
python -m pytest
```

## Acknowledgement

Sentencepiece model used in test is provided by @yoheikikuta. Thanks!
