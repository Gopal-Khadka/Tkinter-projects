from tkinter import *
import os
import qrcode
from pyzbar.pyzbar import decode
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

BG = "#4cc9f0"
H_FONT = ("Arial", 22, "bold")
T_FONT = ("Ubuntu", 18, "normal")


def quit_app():
    if messagebox.askokcancel(
        title="Quit The App", message="Do you want to quit the app?"
    ):
        root.destroy()


def delete_code():
    if messagebox.askokcancel(
        title="Delete the input", message="Do you want to delete the input?"
    ):
        data.delete(0, END)


def qr_code():
    qr_data = data.get()
    if qr_data != str():
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(data=qr_data)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")
        qr_image = ImageTk.PhotoImage(image)
        qr_label.config(image=qr_image)
        qr_label.image = qr_image
        return (True, image)
    else:
        messagebox.showerror(
            title="No data error", message="Don't leave the textbox empty."
        )
        return (False, None)


def save_file():
    is_on, image = qr_code()
    if is_on:
        filepath = filedialog.asksaveasfilename(
            title="Select Location To Save Image",
            initialdir=os.getcwd(),
            filetypes=(("All Files", "*"), ("PNG Files", "*.png")),
        )
        if filepath:
            try:
                image.save(filepath)
            except FileNotFoundError:
                pass


def open_file():
    if data.get()==str():
        data.delete(0, END)
        filepath = filedialog.askopenfilename(
            title="Select Location To Save Image",
            initialdir=os.getcwd(),
            filetypes=(("All Files", "*"), ("PNG Files", "*.png")),
        )
        if filepath:
            try:
                image = Image.open(filepath)
                result = decode(image)
                result = result[0][0]
                data.insert(END, result)
                qr=ImageTk.PhotoImage(image=image)
                qr_label.config(image=qr)
                qr_label.image=qr            
            except IndexError:
                messagebox.showinfo(
                    title="Not A QR Code", message="Uploaded file is not a QR code"
                )
    else:
        if messagebox.askokcancel(title="Save The file First",message="Do you want to save the file first?"):
            save_file()
        else:
            data.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    root.config(bg=BG, padx=20, pady=20)
    root.resizable(False, False)
    root.geometry("500x650+100+40")
    root.title("QR Code App")
    icon = PhotoImage(file="qr_code.png")
    root.iconphoto(False, icon)

    app_heading = Label(root, text="QR Code App", bg=BG, font=H_FONT, fg="#7209b7")
    app_heading.pack()

    # label to show image
    qr_label = Label(root, image=icon, justify=CENTER, bg=BG, width=300, height=300)
    qr_label.pack()
    # imput for qr code data
    data = Entry(root, width=20, fg=BG, justify="center", relief=GROOVE, font=T_FONT)
    data.focus()
    data.place(x=100, y=350)
    # delete image and button
    del_img = PhotoImage(file="delete.png")
    del_button = Button(
        root,
        bd=0,
        fg="#e63946",
        highlightthickness=0,
        image=del_img,
        font=T_FONT,
        command=delete_code,
        bg=BG,
        highlightbackground=BG,
    )
    del_button.place(x=20, y=500, width=64, height=64)
    # open image button
    open = PhotoImage(file="add.png")
    open_button = Button(
        root,
        bd=0,
        fg="#e63946",
        highlightthickness=0,
        image=open,
        font=T_FONT,
        bg=BG,
        command=open_file,
    )
    open_button.place(x=100, y=500, width=64, height=64)
    # qr_code button
    qr_button = Button(
        root,
        bd=0,
        fg="#e63946",
        highlightthickness=0,
        image=icon,
        font=T_FONT,
        command=qr_code,
        bg=BG,
    )
    qr_button.place(x=180, y=500, width=64, height=64)
    # save image and button
    save_img = PhotoImage(file="save.png")
    save_button = Button(
        root,
        bd=0,
        fg="#e63946",
        highlightthickness=0,
        image=save_img,
        font=T_FONT,
        command=save_file,
        bg=BG,
        highlightbackground=BG,
    )
    save_button.place(x=260, y=500, width=64, height=64)
    # quit button
    quit = PhotoImage(file="quit.png")
    quit_button = Button(
        root,
        bd=0,
        fg="#e63946",
        highlightthickness=0,
        image=quit,
        font=T_FONT,
        command=quit_app,
        bg=BG,
    )
    quit_button.place(x=340, y=500, width=60, height=60)
    root.mainloop()
 