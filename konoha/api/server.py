from fastapi import FastAPI

from konoha.api.v1 import tokenization


def create_app() -> FastAPI:
    app = FastAPI()
    app.tokenizers = {}  # type: ignore
    app.include_router(tokenization.router)
    return app
