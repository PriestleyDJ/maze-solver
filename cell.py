from graphics import Line, Point


class Cell:
    def __init__(
        self,
        window=None,
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window

    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._window.draw_line(
                Line(Point(x1, y1), Point(x1, y2)), fill_colour="black"
            )
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._window.draw_line(
                Line(Point(x2, y1), Point(x2, y2)), fill_colour="black"
            )
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._window.draw_line(
                Line(Point(x1, y1), Point(x2, y1)), fill_colour="black"
            )
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._window.draw_line(
                Line(Point(x1, y2), Point(x2, y2)), fill_colour="black"
            )

    def draw_move(self, to_cell, undo=False):
        colour = "red"
        if undo:
            colour = "gray"

        center = ((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        to_center = ((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        connecting_line = Line(
            Point(center[0], center[1]), Point(to_center[0], to_center[1])
        )
        self._window.draw_line(connecting_line, fill_colour=colour)
