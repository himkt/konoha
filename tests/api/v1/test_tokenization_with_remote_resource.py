from typing import Dict
from fastapi.testclient import TestClient

import pytest

from konoha.api.server import create_app


app = create_app()
client = TestClient(app)


@pytest.mark.parametrize(
    "tokenizer_params", [
        {"tokenizer": "mecab", "system_dictionary_path": "s3://konoha-demo/mecab/ipadic"},
    ]
)
def test_tokenization_with_remote_resoruce(tokenizer_params: Dict):
    headers = {"Content-Type": "application/json"}
    params = dict(tokenizer_params, text="私は猫")
    response = client.post("/api/v1/tokenize", headers=headers, json=params)
    assert response.status_code == 200
    assert "tokens" in response.json()
