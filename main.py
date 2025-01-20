#!/usr/bin/env python3

from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
import random

random.seed()


win = Window(800, 600)
num_rows = 10
num_cols = 10

m1 = Maze(125, 25, num_rows, num_cols, 55, 55, win)
#m1.delay = 0.0
m1._break_entrance_and_exit()
m1.break_walls()
#m1.delay = .05

m1.solve()

win.wait_for_close()
