from windows import Line, Point

class Cell:

    def __init__(self,win=None):
        self.has_adjacent_right = True
        self.has_adjacent_left = True
        self.has_top = True
        self.has_bottom = True
        self.visited = False
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self):
        if self.has_adjacent_left ==True:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_adjacent_right == True:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_top == True:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_bottom == True:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
         
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        mid_x = (self._x1 + self._y2) / 2
        mid_y = (self._y1 + self._y2) / 2

        to_mid_x = (to_cell._x1 + to_cell._x2) / 2
        to_mid_y = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, mid_y), Point(mid_x, mid_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_mid_x, to_mid_y), Point(to_cell._x2, to_mid_y))
            self._win.draw_line(line, fill_color)

        elif self._x1 < to_cell._x1:
            line =Line(Point(self._x1, mid_y), Point(self._x2, mid_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_mid_y), Point(to_mid_x, to_mid_y))
            self._win.draw_line(line, fill_color)

        elif self._y1 > to_cell._y1:
            line = Line(Point(mid_x, mid_y), Point(mid_x, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_mid_x, to_cell._y2), Point(to_mid_x, to_mid_y))
            self._win.draw_line(line, fill_color)

        elif self._y1 < to_cell._y1:
            line = Line(Point(mid_x, mid_y), Point(mid_x, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_mid_x, to_mid_y), Point(to_mid_x, to_cell._y1))
            self._win.draw_line(line, fill_color)