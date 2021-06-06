import logging

from fastapi import FastAPI
from rich.logging import RichHandler

from konoha.api.v1 import tokenization
from konoha.api.v1 import batch_tokenization


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)


def create_app() -> FastAPI:
    app = FastAPI()
    app.state.cache = {}
    app.include_router(tokenization.router)
    app.include_router(batch_tokenization.router)
    return app
