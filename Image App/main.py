from tkinter import *
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from random import choice

BG = "#ccffff"
FONT = ("Ubuntu", 18, "normal")


def show_image():
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetypes=(
            ("All Files", "*"),
            ("JPG file", "*.jpg,*.jpeg"),
            ("PNG file", "*.png"),
            ("SVG file","*.svg")
        ),
    )
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    photo.config(image=img)
    photo.image = img
    fileList = filename.split("/")
    root.title(f"Image App -{fileList[-1]}")


if __name__ == "__main__":
    root = Tk()
    root.title("Image Viewer")
    root.config(bg=BG, pady=10, padx=10)
    # icon for app
    icon = PhotoImage(file="icon2.png")
    root.iconphoto(False, icon)
    # gives total value of your pc width and height
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d+50+50" % (width - 100, height - 100))
    root.resizable(False, False)
    # image frame
    img_frame = Frame(root, bg=BG, width=width - 100, height=int(height * 0.6))
    img_frame.place(x=0, y=0)
    # label for showing photo
    photo = Label(img_frame, bg=BG, justify="center")
    photo.pack()
    # frame for buttons
    frame = Frame(root, bg=BG, width=width - 100, height=80)
    frame.place(x=0, y=height - 180)
    # open image
    select_btn = Button(
        frame,
        text="Open Image",
        highlightthickness=0,
        bd=0,
        bg=BG,
        fg="#00e64d",
        font=FONT,
        command=show_image,
    )
    select_btn.place(x=300)
    # exit button
    exit_btn = Button(
        frame,
        text="Exit App",
        highlightthickness=0,
        bd=0,
        bg=BG,
        fg="#da1e37",
        font=FONT,
        command=lambda: root.destroy(),
    )
    exit_btn.place(x=width - 400)

    root.mainloop()
