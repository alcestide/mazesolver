from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Generator")
        self.__root.protocol("WM_DELETEwinDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.width = width
        self.height = height

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y,
                           self.p2.x, self.p2.y,
                           fill=fill_color,
                           width=2)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True

        self.win = win

    def draw(self, x1, y1, x2, y2):
        if self.has_top_wall:
            top = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(top, "black")

        if self.has_right_wall:
            right = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(right, "black")

        if self.has_bottom_wall:
            bottom = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(bottom, "black")

        if self.has_left_wall:
            left = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(left, "black")
        