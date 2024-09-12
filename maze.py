from cell import *
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        if self._window is not None:
            canvas_width = self._window.canvas.winfo_width()
            maze_right_edge = self._x1 + (self._num_cols * self._cell_size_x)
            if maze_right_edge > canvas_width:
                raise ValueError("The specified maze width is too large for the given canvas.")
            
            canvas_height = self._window.canvas.winfo_height()
            maze_bottom_edge = self._y1 + (self._num_rows * self._cell_size_y)
            if maze_bottom_edge > canvas_height:
                raise ValueError("The specified maze height is too large for the given canvas.")


        self._create_cells()


    def _create_cells(self):
        
        self._cells = []

        start_x = self._x1
        start_y = self._y1

        for i in range(self._num_cols):
            column = []
            x1 = start_x
            x2 = start_x + self._cell_size_x

            for j in range(self._num_rows):
                y1 = start_y
                y2 = start_y + self._cell_size_y
                row_cell = Cell(x1, x2, y1, y2, self._window)
                column.append(row_cell)
                start_y = y2

            self._cells.append(column)
            start_x = x2
            start_y = self._y1

        self._draw_cells()
    
    def _draw_cells(self):

        if self._window is not None:

            for column in self._cells:
                for row_cell in column:
                    row_cell.draw(fill_color="red")
                    self._animate()
            


    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)

        