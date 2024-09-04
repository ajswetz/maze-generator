class Line:
    def __init__(self, point_0, point_1):
        self.point_0 = point_0
        self.point_1 = point_1

    def draw(self, canvas, fill_color):

        canvas.create_line(self.point_0.x, self.point_0.y, self.point_1.x, self.point_1.y, fill=fill_color, width=2)
        