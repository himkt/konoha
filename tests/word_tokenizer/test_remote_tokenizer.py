from unittest import mock

from konoha import WordTokenizer


def test_word_tokenize_with_remote_host():
    tokenizer = WordTokenizer(endpoint="localhost:8000/api/v1/tokenize", tokenizer="mecab")
    dummy_tokens = [{"surface": "テスト", "postag": "名詞"}]

    with mock.patch("konoha.WordTokenizer._tokenize_with_remote_host", return_value=dummy_tokens) as mock_obj:
        tokenizer.tokenize("猫は可愛い")
        assert mock_obj.call_args[1]["endpoint"] == "http://localhost:8000/api/v1/tokenize"
        assert mock_obj.call_args[1]["headers"] == {"Content-Type": "application/json"}
        assert mock_obj.call_args[1]["payload"] == {
            "text": "猫は可愛い",
            "tokenizer": "mecab",
            "model_path": None,
            "mode": None,
        }
