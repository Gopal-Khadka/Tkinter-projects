import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
from colorthief import ColorThief
from colorspaces import ColorDetector

H_FONT = ("Arial", 25, "bold")
BG = "white"
color_palette = [
    "#b8255f",
    "#db4035",
    "#ff9933",
    "#fad000",
    "#afb83b",
    "#7ecc40",
    "#299438",
    "#6accbc",
    "#158fad",
    "#14aaf5",
]


def quit_app():
    if messagebox.askokcancel(
        title="Quit The App?", message="Do you want to quit the app?"
    ):
        root.destroy()


def openImage():
    global filepath
    filepath = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        filetypes=(
            ("All Files", "*"),
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpeg,*.jpg"),
        ),
    )
    try:
        file = Image.open(filepath)

    except UnidentifiedImageError:
        messagebox.showerror(
            title="Open Image Only", message="Select image files only."
        )
    except AttributeError:
        pass
    else:
        image = ImageTk.PhotoImage(file)
        img_label.config(image=image)
        img_label.image = image


def find_color():
    if filepath != tuple():
        ct = ColorThief(filepath)
        pallete = ct.get_palette(color_count=11)
        colors = [f"#{rgb[0]:2x}{rgb[1]:2x}{rgb[2]:2x}" for rgb in pallete]

        color_palette = [color.replace(" ", "0") for color in colors]
        canvas1.create_labels(palette=color_palette[0:5])
        canvas2.create_labels(palette=color_palette[5:11])
    else:
        messagebox.showerror(
            title="Open the Image",
            message="Open the image file first to detect the colors",
        )
        openImage()


if __name__ == "__main__":
    root = Tk()
    root.title("Color Detector App")
    root.geometry("800x470")
    root.resizable(False, False)
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)
    Label(root, width=120, height=10, bg="blue").pack()

    frame = Frame(root, width=700, height=370, bg=BG)
    frame.place(x=50, y=50)
    Label(frame, image=icon, bg=BG).place(x=10, y=10)
    Label(frame, text="Color Detector", bg=BG, font=H_FONT).place(x=100, y=20)
    canvas1 = ColorDetector(master=frame, position=(20, 90), palette=color_palette[0:5])
    canvas2 = ColorDetector(
        master=frame, position=(180, 90), palette=color_palette[5:10]
    )

    select_image = Frame(frame, height=350, width=340, bg="#d6dee5")
    select_image.place(x=350, y=10)
    # frame to show images
    img_frame = Frame(
        select_image, height=270, width=320, relief=GROOVE, bg="black", bd=2
    )
    img_frame.place(x=10, y=10)
    img_label = Label(img_frame, bg="black")
    img_label.place(x=0, y=0, height=270, width=310)
    # open image button
    open_img = PhotoImage(file="add.png")
    open_button = Button(
        select_image,
        bg="#d6dee5",
        image=open_img,
        highlightthickness=0,
        command=openImage,
    )
    open_button.place(x=10, y=285, height=64, width=64)
    # find color on image button
    find_img = PhotoImage(file="find.png")
    find_button = Button(
        select_image,
        bg="#d6dee5",
        image=find_img,
        highlightthickness=0,
        command=find_color,
    )
    find_button.place(x=145, y=285, height=64, width=64)
    # quit button
    quit_img = PhotoImage(file="quit.png")
    quit_button = Button(
        select_image,
        bg="#d6dee5",
        image=quit_img,
        highlightthickness=0,
        command=quit_app,
    )
    quit_button.place(x=270, y=285, height=64, width=64)
    root.mainloop()
