from cell import Cell
from time import sleep

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        if num_cols <= 0 or num_rows <= 0:
            raise ValueError("ERROR: num_rows and num_cols must be positive integers")
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells:list[list[Cell]] = []
        for i in range(self._num_cols):
            new_col = []
            for j in range(self._num_rows):
                top_left_x = self._cell_size_x * i + self._x1
                top_left_y = self._cell_size_y * j + self._y1
                new_cell = Cell(
                    top_left_x,
                    top_left_y,
                    top_left_x + self._cell_size_x,
                    top_left_y + self._cell_size_y,
                    self._win
                )
                new_col.append(new_cell)
            self._cells.append(new_col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols -1, self._num_rows -1)