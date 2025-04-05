from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title = "My Title"
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line:Line, fill_color):
        line.draw(self.canvas, fill_color)