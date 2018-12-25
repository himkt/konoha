# Tiny Tokenizer: Basic sentence/word Tokenizer

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
