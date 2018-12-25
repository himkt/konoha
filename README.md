# Tiny Tokenizer: Basic sentence/word Tokenizer

### Quick start: Install tiny_tokenizer using PIP

tiny_tokenizer requires following libraries.
- Python
- MeCab
- KyTea

You can install tiny_tokenizer via pip.
`pip install tiny_tokenizer`

### Quick start: Docker

You can use tiny_tokenizer using the Docker container.
If you want to use tiny_tokenizer with Docker, run following commands.

```
docker build -t himkt/tiny_tokenizer .
docker run -it himkt/tiny_tokenizer
```

### Test

`python -m unittest discover tests`
