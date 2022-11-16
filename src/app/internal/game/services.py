from app.internal.grid.domains import Cell
from app.internal.grid.services import GridService
from app.pkg.errors import BasicError, ErrorObj

from .dto.responses import GameOut


class GameService:
    def __init__(self, grid_service: GridService) -> None:
        self.__grid_service = grid_service

    def create_game(self, height, width) -> None:
        self.__grid_service.create_grid(height=height, width=width)

    def next_step(self) -> tuple[GameOut, None] | tuple[None, ErrorObj]:
        grid = self.__grid_service.get_grid()
        if not grid:
            return None, BasicError.get_not_found_error()
        new_state_container = [None] * (grid.height * grid.width)
        for cell_index in range(len(grid.state_container)):
            current_state = grid.state_container[cell_index]
            cell = Cell.from_index(cell_index=cell_index, height=grid.height, width=grid.width)
            neighbors_count = self.__grid_service.get_cell_neighbors_count(cell, grid)
            new_state = neighbors_count == 2 or neighbors_count == 3 if current_state is True else neighbors_count == 3
            new_state_container[cell_index] = new_state
        self.__grid_service.update_grid(grid, new_state_container)

        if not any(grid.state_container) or grid.state_container == new_state_container:
            return GameOut.from_grid(grid, True), None
        return GameOut.from_grid(grid), None
