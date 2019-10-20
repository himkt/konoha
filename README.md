# tiny_tokenizer

[![Build Status](https://travis-ci.org/himkt/tiny_tokenizer.svg?branch=master)](https://travis-ci.org/himkt/tiny_tokenizer)
[![GitHub stars](https://img.shields.io/github/stars/himkt/tiny_tokenizer.svg?maxAge=2592000&colorB=blue)](https://github.com/himkt/tiny_tokenizer/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/himkt/tiny_tokenizer.svg)](https://github.com/himkt/tiny_tokenizer/issues)
[![GitHub release](https://img.shields.io/github/release/himkt/tiny_tokenizer.svg?maxAge=2592000&colorB=red)](https://github.com/himkt/tiny_tokenizer)
[![MIT License](http://img.shields.io/badge/license-MIT-yellow.svg?style=flat)](LICENSE)

Tiny tokenizer is a simple wrapper of wrapper for Japanese tokenizers.

It unifies the interface of several Japanese tokenizers.

Tiny tokenizer provides you the way to switch a tokenizer and boost your pre-processing.

`tiny_tokenizer` supports following tokenizers.
- MeCab (and [natto-py](https://github.com/buruzaemon/natto-py))
- KyTea (and [Mykytea-python](https://github.com/chezou/Mykytea-python))
- Sudachi ([SudachiPy](https://github.com/WorksApplications/SudachiPy))
- Sentencepiece ([Sentencepiece](https://github.com/google/sentencepiece))
- character-based
- whitespace-based

Also, tiny tokenizer provides a simple rule-based sentence tokenizer,
which segments a document into sentences.


## Installation

### Install tiny_tokenizer on local machine

It is not needed for sentence level tokenization because these libraries are used in word level tokenization.

You can install tiny_tokenizer and above libraries by pip, please run:
`pip install tiny_tokenizer[all]`.

Or, you can install tiny_tokenizer only with SentenceTokenizer by the following command:
`pip install tiny_tokenizer`.


### Install tiny_tokenizer on Docker container

You can use tiny_tokenizer using the Docker container.

If you want to use tiny_tokenizer with Docker, run following commands.

```
docker build -t himkt/tiny_tokenizer .
docker run -it himkt/tiny_tokenizer /bin/bash
```


## Example

### Word level tokenization

- Code

```python
from tiny_tokenizer import WordTokenizer

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
from tiny_tokenizer import SentenceTokenizer

sentence = "私は猫だ。名前なんてものはない。だが，「かわいい。それで十分だろう」。"

tokenizer = SentenceTokenizer()
print(tokenizer.tokenize(sentence))
```

- Output

```
['私は猫だ。', '名前なんてものはない。', 'だが，「かわいい。それで十分だろう」。']
```


## Test

```
python -m pytest
```

## Acknowledgement

Sentencepiece model used in test is provided by @yoheikikuta. Thanks!
