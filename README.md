[![Build Status](https://travis-ci.org/himkt/tiny_tokenizer.svg?branch=master)](https://travis-ci.org/himkt/tiny_tokenizer)
[![GitHub stars](https://img.shields.io/github/stars/himkt/tiny_tokenizer.svg?maxAge=2592000&colorB=blue)](https://github.com/himkt/tiny_tokenizer/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/himkt/tiny_tokenizer.svg)](https://github.com/himkt/tiny_tokenizer/issues)
[![GitHub release](https://img.shields.io/github/release/himkt/tiny_tokenizer.svg?maxAge=2592000&colorB=red)](https://github.com/himkt/tiny_tokenizer)
[![MIT License](http://img.shields.io/badge/license-MIT-yellow.svg?style=flat)](LICENSE)

### Overview

Tiny Tokenizer is simple sentence/word Tokenizer which is convenient to pre-process Japanese text.

<div align="center"><img src="./static/image/tiny_tokenizer.png" width="700"/></div>

### Quick start: Install tiny_tokenizer using PIP

tiny_tokenizer requires following libraries.
- Python
- MeCab (and [natto-py](https://github.com/buruzaemon/natto-py))
- KyTea (and [Mykytea-python](https://github.com/chezou/Mykytea-python))

You can install tiny_tokenizer via pip.
`pip install tiny_tokenizer`

Or, you can install tiny_tokenizer only with SentenceTokenizer by the following command.
`BUILD_WORD_TOKENIZER=0 pip install tiny_tokenizer`


### Quick start: Docker

You can use tiny_tokenizer using the Docker container.
If you want to use tiny_tokenizer with Docker, run following commands.

```
docker build -t himkt/tiny_tokenizer .
docker run -it himkt/tiny_tokenizer
```


### Example

`python3 example/tokenize_document.py`

```
# python3 example/tokenize_document.py
Finish creating word tokenizers

Given document: 我輩は猫である。名前はまだない
#0: 我輩は猫である。
Tokenizer (identity): 我輩は猫である。
Tokenizer (MeCab): 我輩 は 猫 で ある 。
Tokenizer (KyTea): 我輩 は 猫 で あ る 。
Tokenizer (Sentencepiece): ▁ 我 輩 は 猫 である 。
Tokenizer (Character): 我 輩 は 猫 で あ る 。

#1: 名前はまだない
Tokenizer (identity): 名前はまだない
Tokenizer (MeCab): 名前 は まだ ない
Tokenizer (KyTea): 名前 は まだ な い
Tokenizer (Sentencepiece): ▁ 名前 はまだ ない
Tokenizer (Character): 名 前 は ま だ な い
```


### Test

```
python -m pytest
```

### Acknowledgement

Sentencepiece model used in test is provided by @yoheikikuta. Thanks a lot!
