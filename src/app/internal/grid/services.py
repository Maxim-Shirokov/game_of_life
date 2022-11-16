from itertools import product

from app.internal.grid.domains import IGridRepository

from .domains import Cell, Grid


class GridService:
    def __init__(self, repo: IGridRepository) -> None:
        self.__repo = repo

    def create_grid(self, height: int, width: int) -> None:
        self.__repo.create_grid(height=height, width=width)

    def update_grid(self, grid: Grid, new_state_container: list) -> None:
        self.__repo.update_grid(grid, new_state_container)

    def get_grid(self) -> Grid:
        return self.__repo.get_grid()

    def get_cell_neighbors_count(self, cell: Cell, grid: Grid) -> int:
        count = 0
        offsets = product([-1, 0, 1], repeat=2)
        for x_offset, y_offset in offsets:
            if x_offset == 0 and y_offset == 0:
                continue
            neighbor_cell = Cell(x=cell.x + x_offset, y=cell.y + y_offset)
            if not self.check_valid_cell(neighbor_cell, grid):
                continue
            if self.check_alive(neighbor_cell, grid):
                count += 1
            if count > 3:
                return count
        return count

    def check_valid_cell(self, cell: Cell, grid: Grid) -> bool:
        return 0 <= cell.x < grid.width and 0 <= cell.y < grid.height

    def check_alive(self, cell: Cell, grid: Grid) -> bool:
        return grid.state_container[cell.get_cell_index(grid.width)]
