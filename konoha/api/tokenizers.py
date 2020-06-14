from fastapi import APIRouter
from fastapi import Request
from fastapi import HTTPException
from pydantic import BaseModel

import logging
from typing import List
from typing import Optional

from konoha import WordTokenizer


class TokenizeParameter(BaseModel):
    model_path: Optional[str] = None
    text: Optional[str] = None
    texts: Optional[List[str]] = None
    tokenizer: str
    mode: str = "A"


router = APIRouter()
logger = logging.getLogger(__file__)


@router.post("/api/tokenize")
def tokenize(params: TokenizeParameter, request: Request):
    if params.text is not None:
        texts = [params.text]
    elif params.texts is not None:
        texts = params.texts
    else:
        raise HTTPException(status_code=400, detail="text or texts is required.")

    mode = params.mode.lower()
    model_path = (
        "data/model.spm" if params.tokenizer.lower() == "sentencepiece" else None
    )  # NOQA

    signature = f"{params.tokenizer}.{model_path}.{mode}"
    if signature in request.app.tokenizers:
        logging.info(f"Hit cache: {signature}")
        tokenizer = request.app.tokenizers[signature]
    else:
        logging.info(f"Create tokenizer: {signature}")
        try:
            tokenizer = WordTokenizer(
                tokenizer=params.tokenizer,
                with_postag=True,
                model_path=model_path,
                mode=mode,
            )
            request.app.tokenizers[signature] = tokenizer
        except Exception:
            raise HTTPException(status_code=400, detail="fail to initialize tokenizer")

    results = [
        [
            {"surface": t.surface, "part_of_speech": t.postag}
            for t in tokenizer.tokenize(text)
        ]
        for text in texts
    ]

    return {"tokens": results}
