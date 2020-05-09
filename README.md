# 🌿Konoha: Simple wrapper of Japanese Tokenizers

[![GitHub stars](https://img.shields.io/github/stars/himkt/konoha?style=social)](https://github.com/himkt/konoha/stargazers)

![Build Status](https://github.com/himkt/konoha/workflows/Python%20package/badge.svg?style=flat-square)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue?logo=python)
[![GitHub Issues](https://img.shields.io/github/issues/himkt/konoha.svg?cacheSeconds=60&color=yellow)](https://github.com/himkt/konoha/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/himkt/konoha.svg?cacheSeconds=60&color=yellow)](https://github.com/himkt/konoha/issues)
[![GitHub Release](https://img.shields.io/github/release/himkt/konoha.svg?cacheSeconds=60&color=red)](https://github.com/himkt/konoha/releases)

`Konoha` is a Python library for providing easy-to-use integrated interface of various Japanese tokenziers,
which enables you to switch a tokenizer and boost your pre-processing.
Supported tokenizers are character-based tokenizer, whitespace-based tokenizer and followings:

- MeCab (by [natto-py](https://github.com/buruzaemon/natto-py))
- Janome (by [janome](https://github.com/mocobeta/janome))
- KyTea (by [Mykytea-python](https://github.com/chezou/Mykytea-python))
- Sudachi (by [SudachiPy](https://github.com/WorksApplications/SudachiPy))
- Sentencepiece (by [sentencepiece](https://github.com/google/sentencepiece))

Also, `konoha` provides a simple rule-based sentence tokenizer,
which segments a document into sentences.


## Quick Start with Docker

Simply run followings on your computer:

```bash
git clone https://github.com/himkt/konoha  # download konoha
cd konoha && docker-compose up --build  # build and launch contaier
```

Tokenization is done by posting a json object to `localhost:8000/api/tokenize`.
You can also batch tokenize by passing `texts: ["１つ目の入力", "２つ目の入力"]` to the server.

(API documentation is available on `localhost:8000/redoc`, you can check it using your web browser)

Send a request using `curl` on you terminal.

```json
$ curl localhost:8000/api/tokenize -X POST -H "Content-Type: application/json" \
    -d '{"tokenizer": "mecab", "text": "これはペンです"}'

{
  "tokens": [
    [
      {
        "surface": "これ",
        "part_of_speech": "名詞"
      },
      {
        "surface": "は",
        "part_of_speech": "助詞"
      },
      {
        "surface": "ペン",
        "part_of_speech": "名詞"
      },
      {
        "surface": "です",
        "part_of_speech": "助動詞"
      }
    ]
  ]
}
```


## Installation

I recommend you to install konoha by `pip install 'konoha[all]'` or `pip install 'konoha[all_with_integrations]'`.
(`all_with_integrations` will install `AllenNLP`)

- Install konoha with a specific tokenizer: `pip install 'konoha[(tokenizer_name)]`.
- Install konoha with a specific tokenizer and AllenNLP integration: `pip install 'konoha[(tokenizer_name),allennlp]`.
- Install konoha with a specific tokenzier and remote file support: `pip install 'konoha[(tokenizer_name),remote]'`

- Note that SudachiPy requires dictionary. You may have to install dictionary
  - `pip install https://object-storage.tyo2.conoha.io/v1/nc_2520839e1f9641b08211a5c85243124a/sudachi/SudachiDict_core-20191224.tar.gz`
  - [SudachiPy docs](https://github.com/WorksApplications/SudachiPy#step-2-install-sudachidict_core)
  - If you are interested in dictionary, see [SudachiDict docs](https://github.com/WorksApplications/SudachiDict)


## Example

### Word level tokenization

```python
from konoha import WordTokenizer

sentence = '自然言語処理を勉強しています'

tokenizer = WordTokenizer('MeCab')
print(tokenizer.tokenize())
# => [自然, 言語, 処理, を, 勉強, し, て, い, ます]

tokenizer = WordTokenizer('Sentencepiece', model_path="data/model.spm")
print(tokenizer.tokenize(sentence))
# => [▁, 自然, 言語, 処理, を, 勉強, し, ています]
```

For more detail, please see the `example/` directory.

### Remote files

Konoha supports dictionary and model on cloud storage (currently supports Amazon S3).
It requires installing konoha with the `remote` option, see [Installation](#installation).

```python
# download user dictionary from S3
word_tokenizer = WordTokenizer("mecab", user_dictionary_path="s3://abc/xxx.dic")
print(word_tokenizer.tokenize(sentence))

# download system dictionary from S3
word_tokenizer = WordTokenizer("mecab", system_dictionary_path="s3://abc/yyy")
print(word_tokenizer.tokenize(sentence))

# download model file from S3
word_tokenizer = WordTokenizer("sentencepiece", model_path="s3://abc/zzz.model")
print(word_tokenizer.tokenize(sentence))
```

### Sentence level tokenization

```python
from konoha import SentenceTokenizer

sentence = "私は猫だ。名前なんてものはない。だが，「かわいい。それで十分だろう」。"

tokenizer = SentenceTokenizer()
print(tokenizer.tokenize(sentence))
# => ['私は猫だ。', '名前なんてものはない。', 'だが，「かわいい。それで十分だろう」。']
```


## Test

```
python -m pytest
```

## Acknowledgement

Sentencepiece model used in test is provided by @yoheikikuta. Thanks!
