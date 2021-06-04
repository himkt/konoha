from fastapi import FastAPI

from konoha.api.v1 import tokenization
from konoha.api.v1 import batch_tokenization


def create_app() -> FastAPI:
    app = FastAPI()
    app.state.cache = {}
    app.include_router(tokenization.router)
    app.include_router(batch_tokenization.router)
    return app
