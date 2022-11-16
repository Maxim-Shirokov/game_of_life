from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.internal.game.transports import game_router
from config import settings


def get_app_settings() -> dict:
    if settings.DEBUG:
        return dict(debug=True)
    return dict(docs_url=None, redoc_url=None, debug=False, openapi_url=None)


app = FastAPI(**get_app_settings())


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(game_router, prefix='/api')
