from fastapi import Depends

from app.internal.core.db import db

from .repositories import GridRepositoryFake
from .services import GridService


def get_grid_service() -> GridService:
    repo = GridRepositoryFake(db=db)
    return GridService(repo=repo)
