from konoha.api import tokenizers

from fastapi import FastAPI


app = FastAPI()
app.tokenizers = {}  # type: ignore
app.include_router(tokenizers.router)
