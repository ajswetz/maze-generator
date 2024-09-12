from window import *
from point import *
from line import *
from cell import *
from maze import *

def main():

    win = Window(800, 600)
    win.redraw()

    # first_point = Point(0, 0)
    # second_point = Point(800, 600)
    # first_line = Line(first_point, second_point)
    # win.draw_line(first_line, fill_color="red")

    # third_point = Point(0, 600)
    # fourth_point = Point(800, 0)
    # second_line = Line(third_point, fourth_point)
    # win.draw_line(second_line, fill_color="blue")

    # cell_1 = Cell(5, 75, 5, 75, win)
    # cell_1.draw("red")

    # cell_2 = Cell(100, 200, 100, 200, win)
    # cell_2.has_bottom_wall = False
    # cell_2.draw("blue")

    # cell_3 = Cell(400, 500, 100, 200, win)
    # cell_3.has_left_wall = False
    # cell_3.has_right_wall = False
    # cell_3.draw("purple")

    # cell_4 = Cell(200, 300, 400, 500, win)
    # cell_4.has_top_wall = False
    # cell_4.draw("orange")

    # cell_5 = Cell(300, 400, 500, 600, win)
    # cell_5.has_bottom_wall = False
    # cell_5.has_top_wall = False
    # cell_5.has_left_wall = False
    # #cell_5.has_right_wall = False
    # cell_5.draw("black")

    # cell_1.draw_move(cell_2)

    # cell_2.draw_move(cell_3, undo=True)

    # cell_3.draw_move(cell_4)

    # cell_4.draw_move(cell_5, undo=True)

    test_maze = Maze(0, 0, 11, 10, 80, 60, win)

    win.wait_for_close()
    


if __name__ == "__main__":
    main()