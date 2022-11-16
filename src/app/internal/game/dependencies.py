from app.internal.grid.dependencies import get_grid_service

from .services import GameService


def get_game_service() -> GameService:
    grid_service = get_grid_service()
    return GameService(grid_service)
