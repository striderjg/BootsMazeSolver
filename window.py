from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Stides Mazer"
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.isrunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.isrunning = True
        while self.isrunning:
            self.redraw()
    
    def close(self):
        self.isrunning = False
