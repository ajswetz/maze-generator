from window import *
from point import *
from line import *

def main():

    win = Window(800, 600)

    first_point = Point(0, 0)
    second_point = Point(800, 600)
    first_line = Line(first_point, second_point)
    win.draw_line(first_line, fill_color="red")

    third_point = Point(0, 600)
    fourth_point = Point(800, 0)
    second_line = Line(third_point, fourth_point)
    win.draw_line(second_line, fill_color="blue")

    win.wait_for_close()
    


if __name__ == "__main__":
    main()