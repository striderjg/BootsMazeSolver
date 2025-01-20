from point import Point
from line import Line
from window import Window
from tkinter import Canvas

class Cell():
    def __init__(self, pos1: Point, pos2: Point, _win: Window, has_walls: bool ):

        self.top_left = pos1
        self.bottom_right = pos2
        self.top_right = Point(pos2.x, pos1.y)
        self.bottom_left = Point(pos1.x, pos2.y)
        self.wall_color = "black"
        self.undo_color = "red"
        self.path_color = "gray"
        self.bkg_color = "#d9d9d9"
        self.visited = False
        
        self.walls = {}
        self.walls["up"] = Line(self.top_left, self.top_right)
        self.walls["down"] = Line(self.bottom_left, self.bottom_right)
        self.walls["left"] = Line(self.top_left, self.bottom_left)
        self.walls["right"] = Line(self.top_right, self.bottom_right)
        
        self.has_wall = {}
        if has_walls:
            self.has_wall["up"] = True
            self.has_wall["down"] = True
            self.has_wall["left"] = True
            self.has_wall["right"] = True
        else:
            self.has_wall["up"] = self.has_wall["down"] = self.haswall["left"] = self.has_wall["right"] = False

        self._win = _win
    @classmethod
    def with_walls(cls, pos1: Point, pos2: Point, _win: Canvas) -> 'Cell':
        return cls(pos1, pos2, _win, True)
    @classmethod
    def without_walls(cls, pos1: Point, pos2: Point, _win: Canvas) -> 'Cell':
        return cls(pos1, pos2, _win, True)
    
    def remove_wall(self, wall: str):
        if wall not in self.walls:
            raise KeyError(f"wall isn't a valid wall for Cell")
        self.has_wall[wall] = False
    
    def add_wall(self, wall: str):
        if wall not in self.walls:
            raise KeyError(f"wall isn't a valid wall for Cell")
        self.has_wall[wall] = True

    def draw_move(self, to_cell: 'Cell', undo=False):
        if undo:
            color = self.undo_color
        else:
            color = self.path_color

        path = Line(
            Point( self.top_left.x + (self.bottom_right.x-self.top_left.x)/2, self.top_left.y + (self.bottom_right.y - self.top_left.y)/2 ),
            Point( to_cell.top_left.x + (to_cell.bottom_right.x-to_cell.top_left.x)/2, to_cell.top_left.y + (to_cell.bottom_right.y - to_cell.top_left.y)/2 )
        )
        path.draw(self._win.canvas, color)
    
    def set_pos(self, p1: Point, p2: Point):
        self.top_left = p1
        self.bottom_right = p2
        self.top_right = Point(p2.x, p1.y)
        self.bottom_left = Point(p1.x, p2.y)
         
    def draw(self):
        for wall in self.has_wall:
            if self.has_wall[wall]:
                self.walls[wall].draw(self._win.canvas, self.wall_color)
            else:
                self.walls[wall].draw(self._win.canvas, self.bkg_color)

    def _test(self, color):
        for wall in self.has_wall:
            #if self.has_wall[wall]:
            self.walls[wall].draw(self._win.canvas, color)
            #else:
            #    self.walls[wall].draw(self._win.canvas, self.bkg_color)