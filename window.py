from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(master=self.__root, height=height, width=width)
        self.canvas.pack()
        self.is_running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    # def draw_line(self):
    #     self.canvas.create_line(30, 30, 50, 50, fill="red", width=2)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running is True:
            self.redraw()
    
    def close(self):
        self.is_running = False