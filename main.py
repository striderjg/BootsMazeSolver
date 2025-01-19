#!/usr/bin/env python3

from window import Window
from line import Line
from point import Point
from cell import Cell
import random

random.seed()


win = Window(800, 600)

cells = [ ]

for i in range(5):
    cells.append([])
    for j in range(5):
        cells[i].append(Cell.with_walls(
            Point( 10+i*120, 10+j*120 ), Point( (10+i*120) + 100, (10+j*120) + 100 ), win
        ))

for i in range(25):
    for j in ["top", "right", "bottom", "left"]:
        if random.randint(0,1):
            cells[i//5][i%5].remove_wall(j)
for row in cells:
    for cell in row:
        cell.draw()

cells2 = [
    Cell.with_walls( Point( 650, 10), Point(750, 110), win ),
    Cell.with_walls( Point( 650, 120), Point(750, 220), win ),
    Cell.with_walls( Point( 650, 230), Point(750, 330), win ),
    Cell.with_walls( Point( 650, 340), Point(750, 440), win )
]
count = 0
for side in ["top", "right", "bottom", "left"]:
    cells2[count].remove_wall(side)
    cells2[count].draw()
    count += 1

cells[3][4].draw_move(cells[1][2])
cells[0][2].draw_move(cells[3][3], True)


'''
win.draw_line(
    Line(
    Point(20,20),
    Point(60, 100)),
    "black"
)
win.draw_line(
    Line(
    Point(60,20),
    Point(20, 100)),
    "black"
)
win.draw_line(
    Line(
    Point(300,200),
    Point(600, 200)),
    "black"
)
'''
win.wait_for_close()
