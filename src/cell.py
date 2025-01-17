from graphics import Point, Line

class Cell():
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def get_center(self):
        center = Point(self._x1 + ((self._x2 - self._x1) / 2), ((self._y2 - self._y1) / 2) + self._y1)
        return center
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self._win is None:
            return

        first = Point(self._x1, self._y1)
        second = Point(self._x1, self._y2)
        
        if self.has_left_wall:
            self._win.draw_line(Line(first, second), "black")
        else:
            self._win.draw_line(Line(first, second), "white")
        
        first = Point(self._x1, self._y1)
        second = Point(self._x2, self._y1)

        if self.has_top_wall:
            self._win.draw_line(Line(first, second), "black")
        else:
            self._win.draw_line(Line(first, second), "white")

        first = Point(self._x2, self._y1)
        second = Point(self._x2, self._y2)
        
        if self.has_right_wall:
            self._win.draw_line(Line(first, second), "black")
        else:
            self._win.draw_line(Line(first, second), "white")
        
        first = Point(self._x1, self._y2)
        second = Point(self._x2, self._y2)

        if self.has_bottom_wall:
            self._win.draw_line(Line(first, second), "black")
        else:
            self._win.draw_line(Line(first, second), "white")
    
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        first = self.get_center()
        second = to_cell.get_center()

        self._win.draw_line(Line(first, second), fill_color)


        
