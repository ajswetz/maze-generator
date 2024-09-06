from tkinter import Tk, BOTH, Canvas
from point import *
from line import *

class Cell:
    def __init__(self, x1, x2, y1, y2, window):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, fill_color):

        smaller_x = min(self._x1, self._x2)
        greater_x = max(self._x1, self._x2)
        smaller_y = min(self._y1, self._y2)
        greater_y = max(self._y1, self._y2)

        up_left_corner = Point(smaller_x, smaller_y)
        up_right_corner = Point(greater_x, smaller_y)
        bot_left_corner = Point(smaller_x, greater_y)
        bot_right_corner = Point(greater_x, greater_y)

        if self.has_left_wall:
            left_wall = Line(up_left_corner, bot_left_corner)
            left_wall.draw(self._win.canvas, fill_color)

        if self.has_right_wall:
            right_wall = Line(up_right_corner, bot_right_corner)
            right_wall.draw(self._win.canvas, fill_color)

        if self.has_top_wall:
            top_wall = Line(up_left_corner, up_right_corner)
            top_wall.draw(self._win.canvas, fill_color)

        if self.has_bottom_wall:
            bottom_wall = Line(bot_left_corner, bot_right_corner)
            bottom_wall.draw(self._win.canvas, fill_color)