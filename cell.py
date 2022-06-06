from windows import Line, Point

class Cell:

    def __init__(self,win=None):
        self.has_adjacent_right = True
        self.has_adjacent_left = True
        self.has_top = True
        self.has_bottom = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self,x1,y1,x2,y2): # Initialize coordinates
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_adjacent_left: # Coordinates for left wall
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line, "white")
        if self.has_adjacent_right: # Coordinates for right wall
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_top:            # Coordinates for top wall
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2,y1))
            self._win.draw_line(line, "white")
        if self.has_bottom:         # Coordinates for bottom wall 
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2, y2))
            self._win.draw_line(line, "white")
         
    def draw_move(self, to_cell, undo=False): # Draw all the moves
        if self._win is None:
            return
        mid_x = (self._x1 + self._y2) / 2     # Described as the middle of the cells
        mid_y = (self._y1 + self._y2) / 2

        to_mid_x = (to_cell._x1 + to_cell._x2) / 2
        to_mid_y = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "green"
        if undo:
            fill_color = "red"

        if self._x1 > to_cell._x1: # Move to the left
            line = Line(Point(self._x1, mid_y), Point(mid_x, mid_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_mid_x, to_mid_y), Point(to_cell._x2, to_mid_y))
            self._win.draw_line(line, fill_color)

        elif self._x1 < to_cell._x1: # Move to the right
            line =Line(Point(self._x1, mid_y), Point(self._x2, mid_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_mid_y), Point(to_mid_x, to_mid_y))
            self._win.draw_line(line, fill_color)

        elif self._y1 > to_cell._y1: # Move up
            line = Line(Point(mid_x, mid_y), Point(mid_x, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_mid_x, to_cell._y2), Point(to_mid_x, to_mid_y))
            self._win.draw_line(line, fill_color)

        elif self._y1 < to_cell._y1: # Move down
            line = Line(Point(mid_x, mid_y), Point(mid_x, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_mid_x, to_mid_y), Point(to_mid_x, to_cell._y1))
            self._win.draw_line(line, fill_color)