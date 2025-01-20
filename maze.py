from window import Window
from cell import Cell
from point import Point
from time import sleep
import random

class Maze():
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_width: int, cell_height: int, _win: Window = None, seed:int = None) -> 'Maze':
        self.posx = x1
        self.posy = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.end = { "x":num_cols-1, "y": num_rows-1}
        self.cell_width = cell_width
        self.cell_height = cell_height
        self._win = _win
        if seed != None:
            random.seed(seed)
        self.delay = .05

        self._create_cells()

    def _break_entrance_and_exit(self):
        self._cells[0][0].remove_wall("left")
        self._cells[self.num_cols-1][self.num_rows-1].remove_wall("right")
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def break_walls(self):
        #self.delay = .2
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i:int, j:int) -> bool:
        self._animate()
        self._cells[i][j].visited = True
        if(i == self.end['x'] and j == self.end['y']):
            return True
        for dir in ["up", "down", "left", "right"]:
            new_i, new_j = self._get_adj_cell(i, j, dir)
            if self._isCell(new_i, new_j) and not self._cells[new_i][new_j].visited and not self._cells[i][j].has_wall[dir]:
                self._cells[i][j].draw_move(self._cells[new_i][new_j])
                if(self._solve_r(new_i, new_j)):
                    return True
                self._cells[i][j].draw_move(self._cells[new_i][new_j], True)
        return False

    def _isCell(self, i:int, j:int) -> bool:
        if(i >= 0 and i <= self.num_cols-1 and j >= 0 and j <= self.num_rows-1):
            return True
        return False
    
    def _get_adj_cell(self, i:int, j:int, dir:str):
        match dir:
            case "up":
                return (i, j-1)
            case "down":
                return (i, j+1)
            case "left":
                return (i-1, j)
            case "right":
                return (i+1, j)
        
    def _test(self, i, j, color):
        self._cells[i][j]._test(color)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Find unvisited adjasent
            if(i != 0 and not self._cells[i-1][j].visited):
                to_visit.append( (i-1, j) )

            if(i < self.num_cols-1 and not self._cells[i+1][j].visited):
                to_visit.append( (i+1, j) )

            if(j != 0 and not self._cells[i][j-1].visited ):
                to_visit.append( (i, j-1) )
            
            if(j < self.num_rows-1 and not self._cells[i][j+1].visited):
                to_visit.append( (i, j+1) )

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            choice = random.choice(to_visit)
            to_visit.remove((choice))
            new_i, new_j = choice

            # remove walls
            # down
            if(new_j > j):
                self._cells[i][j].remove_wall("down")
                self._cells[new_i][new_j].remove_wall("up")
            # up
            elif(new_j < j):
                self._cells[i][j].remove_wall("up")
                self._cells[new_i][new_j].remove_wall("down")
            # right
            elif(new_i > i):
                self._cells[i][j].remove_wall("right")
                self._cells[new_i][new_j].remove_wall("left")
            # left
            elif(new_i < i):
                self._cells[i][j].remove_wall("left")
                self._cells[new_i][new_j].remove_wall("right")

            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
             
    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                p1 = Point( self.posx + col*self.cell_width, self.posy + row*self.cell_height )
                p2 = Point( self.posx + (col+1)*self.cell_width, self.posy + (row+1)*self.cell_height)
                self._cells[col].append( Cell.with_walls(p1, p2, self._win) )
        for cell in range(self.num_cols * self.num_rows):
            self._draw_cell(cell%self.num_cols, cell//self.num_cols)
        #for i in range(self.num_cols):
        #    for j in range(self.num_rows):
        #        self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        if self._win == None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(self.delay)
