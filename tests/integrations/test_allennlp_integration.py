import tempfile
from typing import List, Optional

import allennlp.commands.train
from allennlp.models.basic_classifier import BasicClassifier

import pytest

from konoha.integrations.allennlp import KonohaTokenizer


@pytest.fixture
def raw_text():
    return "吾輩は猫である"


@pytest.mark.parametrize(
    "token_surfaces,tokenizer_name,mode,model_path", (
        ("吾輩 は 猫 で ある".split(" "), "mecab", None, None),
        ("吾輩 は 猫 で ある".split(" "), "janome", None, None),
        ("吾輩 は 猫 で あ る".split(" "), "kytea", None, None),
        ("▁ 吾 輩 は 猫 である".split(" "), "sentencepiece", None, "data/model.spm"),
        ("吾輩 は 猫 で ある".split(" "), "sudachi", "A", None),
    )
)
def test_allennlp(
    raw_text: str,
    token_surfaces: List[str],
    tokenizer_name: str,
    mode: Optional[str],
    model_path: Optional[str],
) -> None:
    tokenizer = KonohaTokenizer(
        tokenizer_name=tokenizer_name,
        mode=mode,
        model_path=model_path,
    )
    tokens_konoha = tokenizer.tokenize(raw_text)
    assert token_surfaces == list(t.text for t in tokens_konoha)


def test_allennlp_training():
    with tempfile.TemporaryDirectory() as serialization_dir:
        model = allennlp.commands.train.train_model_from_file(
            "test_fixtures/classifier.jsonnet",
            serialization_dir=serialization_dir,
        )
        assert isinstance(model, BasicClassifier)
