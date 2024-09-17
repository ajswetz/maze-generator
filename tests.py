import unittest
from maze import *
from window import *

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 5
        num_rows = 7
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_3(self):
        num_cols = 3
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_too_wide(self):
        win = Window(800, 600)
        win.redraw()
        self.assertRaises(ValueError, Maze, x1=0, y1=0, num_rows=2, num_cols=100, cell_size_x=100, cell_size_y=10, window=win)

    def test_maze_too_high(self):
        win = Window(800, 600)
        win.redraw()
        self.assertRaises(ValueError, Maze, x1=0, y1=0, num_rows=100, num_cols=5, cell_size_x=10, cell_size_y=100, window=win)

    def test_break_entrance_exit(self):
        m1 = Maze(0, 0, 3, 2, 10, 10)
        m1._break_entrance_and_exit()

        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 3, 2, 10, 10)
        for column in m1._cells:
            for row_cell in column:
                row_cell.visited = True

        m1._reset_cells_visited()
        self.assertFalse(m1._cells[0][0].visited)
        self.assertFalse(m1._cells[1][1].visited)
        self.assertFalse(m1._cells[-1][-1].visited)


if __name__ == "__main__":
    unittest.main()