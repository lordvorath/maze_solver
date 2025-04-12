import random
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
        seed=None
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
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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

    def _break_walls_r(self, i:int, j:int):
        # print(f"Visiting: {i}, {j}")
        current = self._cells[i][j]
        current.visited = True
        # self._draw_cell(i, j)
        while True:
            to_visit = []
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1,j)) 
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if i < self._num_cols - 1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if j < self._num_rows -1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            going_to = random.randrange(0, len(to_visit))
            new_x:int = to_visit[going_to][0]
            new_y:int = to_visit[going_to][1]
            if new_x > i:
                self._cells[i][j].has_right_wall = False
                self._cells[new_x][new_y].has_left_wall = False
            elif new_x < i:
                self._cells[i][j].has_left_wall = False
                self._cells[new_x][new_y].has_right_wall = False
            if new_y > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_x][new_y].has_top_wall = False
            elif new_y < j:
                self._cells[i][j].has_top_wall = False
                self._cells[new_x][new_y].has_bottom_wall = False
            self._break_walls_r(new_x, new_y)
            