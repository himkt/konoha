import logging
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from pydantic import BaseModel

from konoha import WordTokenizer


class TokenizeParameter(BaseModel):
    tokenizer: str = "MeCab"
    user_dictionary_path: Optional[str] = None
    system_dictionary_path: Optional[str] = None
    model_path: Optional[str] = None
    mode: Optional[str] = "A"
    dictionary_format: Optional[str] = None
    text: Optional[str] = None
    texts: Optional[List[str]] = None


router = APIRouter()
logger = logging.getLogger(__file__)


def generate_cache_key(params):
    params = params.dict(exclude={"text", "texts"})
    return ".".join(f"{k}-{v}" for k, v in params.items())


@router.post("/api/v1/tokenize")
async def tokenize(params: TokenizeParameter, request: Request):
    if params.texts is not None:
        message = (
            "A parameter `texts` is now unacceptable for /api/v1/tokenize."
            " Please use /api/v1/batch_tokenize instead."
        )
        raise HTTPException(status_code=400, detail=message)

    if params.text is None:
        raise HTTPException(status_code=400, detail="text or texts is required.")

    cache_key = generate_cache_key(params)
    if cache_key in request.app.state.cache:
        logging.info(f"Hit cache: {cache_key}")
        tokenizer = request.app.state.cache[cache_key]
    else:
        logging.info(f"Create tokenizer: {cache_key}")
        try:
            tokenizer = WordTokenizer(
                tokenizer=params.tokenizer,
                user_dictionary_path=params.user_dictionary_path,
                system_dictionary_path=params.system_dictionary_path,
                model_path=params.model_path,
                mode=params.mode,
                dictionary_format=params.dictionary_format,
            )
            request.app.state.cache[cache_key] = tokenizer
        except Exception:
            raise HTTPException(status_code=400, detail="fail to initialize tokenizer")

    tokens = [token.dict() for token in tokenizer.tokenize(params.text)]
    return {"tokens": tokens}
