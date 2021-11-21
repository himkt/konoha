import os
from typing import Dict
import sys

import pytest
from fastapi.testclient import TestClient

from konoha.api.server import create_app

app = create_app()
client = TestClient(app)


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab"},
        {"tokenizer": "sudachi", "mode": "A"},
        {"tokenizer": "sudachi", "mode": "B"},
        {"tokenizer": "sudachi", "mode": "C"},
        {"tokenizer": "sentencepiece", "model_path": "data/model.spm"},
        {"tokenizer": "kytea", "model_path": "data/model.knm"},
        {"tokenizer": "character"},
        {"tokenizer": "nagisa"},
        {"tokenizer": "janome"},
    ]
)
def test_tokenization(tokenizer_params: Dict):
    if tokenizer_params["tokenizer"] == "kytea" and sys.version_info < (3, 7):
        pytest.skip("KyTea doesn't work in Python3.6")

    headers = {"Content-Type": "application/json"}
    params = dict(tokenizer_params, texts=["私は猫", "あなたは犬"])
    response = client.post("/api/v1/batch_tokenize", headers=headers, json=params)
    assert response.status_code == 200
    assert "tokens_list" in response.json()


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab", "system_dictionary_path": "s3://konoha-demo/mecab/ipadic"},
    ]
)
def test_tokenization_with_remote_resource(tokenizer_params: Dict):
    if "AWS_ACCESS_KEY_ID" not in os.environ and tokenizer_params["system_dictionary_path"].startswith("s3://"):
        pytest.skip("AWS credentials not found.")

    headers = {"Content-Type": "application/json"}
    params = dict(tokenizer_params, texts=["私は猫", "あなたは犬"])
    response = client.post("/api/v1/batch_tokenize", headers=headers, json=params)
    assert response.status_code == 200
    assert "tokens_list" in response.json()
