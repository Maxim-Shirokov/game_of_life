from typing import Protocol, Self

from pydantic import BaseModel


class Grid(BaseModel):
    height: int
    width: int
    state_container: list[bool] = None


class Cell(BaseModel):
    x: int
    y: int

    @classmethod
    def from_index(cls, cell_index: int, height: int, width: int) -> Self:
        return cls(x=cell_index % width, y=cell_index // height)

    def get_cell_index(self, width: int) -> int:
        return self.y * width + self.x


class IGridRepository(Protocol):
    def create_grid(self, height: int, width: int) -> None:
        ...

    def update_grid(self, grid: Grid, new_state_container: list) -> None:
        ...

    def get_grid(self) -> Grid:
        ...
