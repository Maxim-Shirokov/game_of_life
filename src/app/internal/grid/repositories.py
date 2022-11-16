import random

from .domains import Cell, Grid


class GridRepositoryFake:
    def __init__(self, db):
        self.db = db

    def create_grid(self, height: int, width: int) -> None:
        self.db.current_state = [bool(random.randint(0, 1)) for _ in range(height * width)]
        self.db.height = height
        self.db.width = width

    def update_grid(self, grid: Grid, new_state_container: list) -> None:
        self.db.current_state = new_state_container

    def get_grid(self) -> Grid | None:
        if not getattr(self.db, 'current_state', None):
            return None
        return Grid(height=self.db.height, width=self.db.width, state_container=self.db.current_state)
