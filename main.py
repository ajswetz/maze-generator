from window import *
from point import *
from line import *
from cell import *
from maze import *

def main():

    win = Window(1000, 1000)
    win.redraw()

    test_maze = Maze(x1=10, y1=10, num_rows=18, num_cols=15, cell_size_x=50, cell_size_y=50, window=win, seed=None)

    test_maze._break_entrance_and_exit()

    test_maze._break_walls_r(0, 0)

    test_maze._reset_cells_visited()

    test_maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()