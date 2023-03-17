from tkinter import *
BG = "white"
T_FONT = ("Arial", 15, "bold")



class ColorDetector:
    def __init__(self, master, position: tuple,palette:list) -> None:
        self.master = master
        self.x = position[0]
        self.y = position[1]
        self.canvas = Canvas(self.master, height=265, width=150, bd=0, bg=BG)
        self.canvas.place(x=self.x, y=self.y)
        self.create_labels(palette)

    def create_labels(self, palette):

        for i in range(5):
            x = 50
            self.color = self.canvas.create_rectangle(
                (10, 10 + i * x, 50, (i + 1) * x), fill=palette[i]
            )
            self.hex = Label(self.canvas, text=palette[i], font=T_FONT, bg=BG,width=7)
            self.hex.place(x=60, y=15 + i * x)
