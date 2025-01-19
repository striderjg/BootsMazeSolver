#!/usr/bin/env python3

from window import Window
from line import Line
from point import Point

win = Window(800, 600)
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


win.wait_for_close()
