from typing import Self

from pydantic import BaseModel

from app.internal.grid.domains import Grid


class GameOut(BaseModel):
    state: list[list[bool]]
    game_over: bool

    @classmethod
    def from_grid(cls, grid: Grid, game_over: bool = False) -> Self:
        return cls(
            state=[grid.state_container[i : i + grid.width] for i in range(0, len(grid.state_container), grid.width)],
            game_over=game_over,
        )
