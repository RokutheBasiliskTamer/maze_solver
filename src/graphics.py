from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack()
        self._is_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()
    
    def close(self):
        self._is_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x: {self.x}, y:{self.y})"

class Line():
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.first_point.x, self.first_point.y,
                           self.second_point.x, self.second_point.y,
                           fill = fill_color, width = 2)
