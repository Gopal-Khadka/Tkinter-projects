from tkinter import *
from tkinter import ttk

BG = "#f2f3f5"
root = Tk()
root.title("WHITEBOARD GUI")
root.geometry("1050x600+150+50")
root.resizable(FALSE, FALSE)
root.config(bg=BG)

current_x = 0
current_y = 0
color = "black"


def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y


def show_color(new_color):
    global color
    color = new_color


def addLine(work):
    global current_x, current_y
    canvas.create_line(
        (current_x, current_y, work.x, work.y),
        fill=color,
        width=int(width.get()),
        capstyle=ROUND,
        smooth=True,
    )
    current_x, current_y = work.x, work.y


def new_canvas():
    canvas.delete("all")
    display_palette()


def use_color():
    color = str(color_value.get())
    show_color(color)


def display_palette():
    id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("black"))

    id = colors.create_rectangle((10, 40, 30, 60), fill="gray")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("gray"))

    id = colors.create_rectangle((10, 70, 30, 90), fill="red")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

    id = colors.create_rectangle((10, 100, 30, 120), fill="brown4")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("brown4"))

    id = colors.create_rectangle((10, 130, 30, 150), fill="orange")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))

    id = colors.create_rectangle((10, 160, 30, 180), fill="yellow")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

    id = colors.create_rectangle((10, 190, 30, 210), fill="blue")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

    id = colors.create_rectangle((10, 220, 30, 240), fill="purple")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("purple"))

    id = colors.create_rectangle((10, 250, 30, 270), fill="green")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("green"))

    id = colors.create_rectangle((10, 280, 30, 300), fill="pink")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("pink"))


# icon img
iconimg = PhotoImage(file="icon.png")
root.iconphoto(False, iconimg)
# eraser button
eraserimg = PhotoImage(file="eraser1.png")
eraser = Button(image=eraserimg, bg="#f2f3f5", command=new_canvas)
eraser.place(x=32, y=400)
# width label
width_label = Label(width=5, text="Width", bg="#f2f3f5")
width_label.place(x=30, y=460)
# width of color
width = Entry(width=5, bg="#f2f3f5")
width.insert(0, "1")
width.focus()
width.place(x=32, y=435)
# color value of color
color_btn = Button(width=5, text="Use Color", bg="#f2f3f5", command=use_color)
color_btn.place(x=30, y=510)
# width of color
color_value = Entry(width=5, bg="#f2f3f5")
color_value.insert(0, color)
color_value.place(x=32, y=485)


# color canvas
colors = Canvas(root, bg="white", height=300, width=37, bd=0)
colors.place(x=30, y=60)
# canvas
canvas = Canvas(root, bg="white", height=500, width=930, bd=0, cursor="hand2")
canvas.place(x=100, y=10)
canvas.bind("<Button-1>", locate_xy)
canvas.bind("<B1-Motion>", addLine)


if __name__ == "__main__":
    display_palette()

root.mainloop()
