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
            window
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

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
        for column in self._cells:
            for row_cell in column:
                row_cell.draw(fill_color="red")
                self._animate()
        


    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)

        