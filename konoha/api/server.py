from fastapi import FastAPI

from konoha.api import tokenizers

app = FastAPI()
app.tokenizers = {}  # type: ignore
app.include_router(tokenizers.router)
