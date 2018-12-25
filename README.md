[![Build Status](https://travis-ci.org/himkt/tiny_tokenizer.svg?branch=master)](https://travis-ci.org/himkt/tiny_tokenizer)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/himkt/tiny_tokenizer.svg)](https://github.com/himkt/tiny_tokenizer/issues)
[![GitHub stars](https://img.shields.io/github/stars/himkt/tiny_tokenizer.svg)](https://github.com/himkt/tiny_tokenizer/stargazers)
[![GitHub release](https://img.shields.io/github/release/qubyte/rubidium.svg?maxAge=2592000)](https://github.com/himkt/tiny_tokenizer)
[![GitHub commits](https://img.shields.io/github/commits-since/SubtitleEdit/subtitleedit/3.4.7.svg?maxAge=2592000)](https://github.com/himkt/tiny_tokenizer)

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
我輩は猫である。
words: MeCab
  我輩
  は
  猫
  で
  ある
  。
words: KyTea
  我輩
  は
  猫
  で
  あ
  る
  。
名前はまだない
words: MeCab
  名前
  は
  まだ
  ない
words: KyTea
  名前
  は
  まだ
  な
  い
```

### Test

`python -m unittest discover tests`
