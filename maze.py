from cell import *
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None,
            seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._seed = seed

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

        if self._seed is not None:
            random.seed(self._seed)


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
        time.sleep(0.1)


    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False


        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False

        if self._window is not None:

            entrance_cell.draw(fill_color="red")
            self._window.redraw()
            
            exit_cell.draw(fill_color="red")
            self._window.redraw()

        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            cells_to_visit = []
            
            #get above: i = i; j = j-1
            if j-1 > 0:
                above = (i, j-1)
                if self._cells[i][j-1].visited == False:
                    cells_to_visit.append(above)

            #get below: i = i; j = j+1
            if j+1 < self._num_rows:
                below = (i, j+1)
                if self._cells[i][j+1].visited == False:
                    cells_to_visit.append(below)

            #get left: i = i-1, j = j
            if i-1 > 0:
                left = (i-1, j)
                if self._cells[i-1][j].visited == False:
                    cells_to_visit.append(left)

            #get right: i = i+1, j = j
            if i+1 < self._num_cols:
                right = (i+1, j)
                if self._cells[i+1][j].visited == False:
                    cells_to_visit.append(right)

            if len(cells_to_visit) == 0:
                self._cells[i][j].draw(fill_color="red")
                return
            else: