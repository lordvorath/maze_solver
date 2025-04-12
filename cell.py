from point import Point
from line import Line
from window import Window

class Cell():
    def __init__(self, x1, y1, x2, y2, win:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.top_left = Point(self._x1, self._y1)
        self.bottom_right = Point(self._x2, self._y2)

    def draw(self, top_left = None, bottom_right = None):
        if self._win is None:
            return
        if top_left is None:
            top_left = self.top_left
        if bottom_right is None:
            bottom_right = self.bottom_right
        if self.has_left_wall:
            self._win.draw_line(Line(
                Point(top_left.x, top_left.y),
                Point(top_left.x, bottom_right.y),
                
            ), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(
                Point(bottom_right.x, top_left.y),
                Point(bottom_right.x, bottom_right.y)
            ), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(
                Point(top_left.x, top_left.y),
                Point(bottom_right.x, top_left.y)
            ), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(
                Point(top_left.x, bottom_right.y),
                Point(bottom_right.x, bottom_right.y)
            ), "black")

    def draw_move(self, to_cell, undo=False):
        start = Point(
            (self._x1 + self._x2)  / 2,
            (self._y1 + self._y2)  / 2,
            )
        end = Point(
            (to_cell._x1 + to_cell._x2) / 2,
            (to_cell._y1 + to_cell._y2) / 2,
        )
        if undo:
            color = "gray"
        else:
            color = "red"
        self._win.draw_line(Line(
            start, end
        ), color)