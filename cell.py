from tkinter import Tk, BOTH, Canvas
from point import *
from line import *

class Cell:
    def __init__(self, x1, x2, y1, y2, window=None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

        self.visited = False

        self._center_x = (self._x1 + self._x2) / 2
        self._center_y = (self._y1 + self._y2) / 2
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, fill_color="red"):

        if self._win is not None:

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
            elif not self.has_left_wall:
                left_wall = Line(up_left_corner, bot_left_corner)
                left_wall.draw(self._win.canvas, fill_color="#d9d9d9")

            if self.has_right_wall:
                right_wall = Line(up_right_corner, bot_right_corner)
                right_wall.draw(self._win.canvas, fill_color)
            elif not self.has_right_wall:
                right_wall = Line(up_right_corner, bot_right_corner)
                right_wall.draw(self._win.canvas, fill_color="#d9d9d9")               

            if self.has_top_wall:
                top_wall = Line(up_left_corner, up_right_corner)
                top_wall.draw(self._win.canvas, fill_color)
            elif not self.has_top_wall:
                top_wall = Line(up_left_corner, up_right_corner)
                top_wall.draw(self._win.canvas, fill_color="#d9d9d9")                

            if self.has_bottom_wall:
                bottom_wall = Line(bot_left_corner, bot_right_corner)
                bottom_wall.draw(self._win.canvas, fill_color)
            elif not self.has_bottom_wall:
                bottom_wall = Line(bot_left_corner, bot_right_corner)
                bottom_wall.draw(self._win.canvas, fill_color="#d9d9d9")

    def draw_move(self, to_cell, undo=False):

        if self._win is not None:

            from_center_point = Point(self._center_x, self._center_y)
            to_center_point = Point(to_cell._center_x, to_cell._center_y)
            
            if undo is False:
                fill_color = "red"
            if undo is True:
                fill_color = "gray"

            connecting_line = Line(from_center_point, to_center_point)
            connecting_line.draw(self._win.canvas, fill_color)

    def __repr__(self) -> str:
        return f"Cell object at x: {self._x1},{self._x2} | y: {self._y1},{self._y2}"