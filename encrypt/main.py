import base64
from tkinter import *
from tkinter import messagebox

BG = "#fff"
H_FONT = ("Arial", 15, "bold")
B_FONT = ("Poppins", 12, "normal")
T_FONT = ("Ubuntu", 13, "normal")


def encrypt():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(root)
        screen1.title("Encryption")
        screen1.geometry("420x300")
        screen1.resizable(False, False)
        message = str(encrypt_text.get(1.0, END))
        encode_msg = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_msg)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="Encrypted message", font=T_FONT).pack()
        final = Text(screen1, bd=0, relief=GROOVE, wrap=WORD, font=T_FONT)
        final.pack()
        final.insert(END, encrypt)

    elif password == "":
        messagebox.showerror(title="Encryption", message="Please Input Password")

    elif password != "1234":
        messagebox.showerror(
            title="Encryption", message="Please Input Correct Password"
        )
    


def decrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(root)
        screen2.title("Encryption")
        screen2.geometry("420x300")
        screen2.resizable(False, False)
        message = str(encrypt_text.get(1.0, END))
        decode_msg = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_msg)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="Encrypted message", font=T_FONT).pack()
        final = Text(screen2, bd=0, relief=GROOVE, wrap=WORD, font=T_FONT)
        final.pack()
        final.insert(END, decrypt)

    elif password == "":
        messagebox.showerror(title="Encryption", message="Please Input Password")

    elif password != "1234":
        messagebox.showerror(
            title="Encryption", message="Please Input Correct Password"
        )


def clear():
    encrypt_text.delete(1.0, END)


def quit_app():
    if messagebox.askokcancel(title="Quit App", message="Do you want to quit app?"):
        root.destroy()


if __name__ == "__main__":

    root = Tk()
    root.title("Encryptor and Decryptor")
    root.config(bg=BG, pady=10, padx=20)
    root.geometry("650x500")
    root.resizable(FALSE, FALSE)
    img = PhotoImage(file="key.png")
    root.iconphoto(False, img)

    decrypt_label = Label(
        root, text="Enter text below to encrypt and decrypt:", bg=BG, font=H_FONT
    )
    decrypt_label.pack()

    encrypt_text = Text(root, width=75, height=10, bg=BG, padx=10, font=T_FONT)
    encrypt_text.focus()
    encrypt_text.insert(1.0, "SAMPLE TEXT")
    encrypt_text.pack()

    secret_label = Label(
        root, text="Enter secret pass for encode/decode:", bg=BG, font=H_FONT, padx=20
    )
    secret_label.pack()

    code = StringVar()
    secret_pass = Entry(width=25, textvariable=code, show="*", font=T_FONT)
    secret_pass.place(height=30, width=300, x=150, y=300)

    encrypt_btn = Button(
        root,
        text="ENCRYPT",
        height=2,
        width=15,
        font=B_FONT,
        highlightthickness=0,
        bg="#ed3833",
        fg=BG,
        command=encrypt,
    )
    encrypt_btn.place(x=5, y=350)

    decrypt_btn = Button(
        root,
        text="DECRYPT",
        height=2,
        width=15,
        highlightthickness=0,
        font=B_FONT,
        bg="#00bd56",
        fg=BG,
        command=decrypt,
    )
    decrypt_btn.place(x=210, y=350)

    clear_btn = Button(
        root,
        text="CLEAR",
        height=2,
        width=15,
        highlightthickness=0,
        font=B_FONT,
        bg="#1089ff",
        fg=BG,
        command=clear,
    )
    clear_btn.place(x=430, y=350)

    quit_btn = Button(
        root,
        text="QUIT",
        height=2,
        width=25,
        highlightthickness=0,
        font=B_FONT,
        bg="#ed3833",
        fg=BG,
        command=quit_app,
    )
    quit_btn.place(x=150, y=430)

    root.mainloop()
