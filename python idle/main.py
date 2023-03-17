import subprocess
from tkinter import *
from tkinter import filedialog, messagebox
import os

BG = "#111d13"
FONT = ("Ubuntu", 15, "normal")
filePath = ""


def quit_app(event=None):
    if messagebox.askokcancel(
        title="Quit The App", message="Are you sure to quit the app?"
    ):
        root.destroy()


def delete_code(event=None):
    code = code_box.get(1.0, END)
    if len(code) != 1:
        if messagebox.askokcancel(
            title="Clear The Code", message="Are you sure to clear the code?"
        ):
            code_box.delete(1.0, END)


def open_file(event=None):
    global filePath
    path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select The File",
        filetypes=(
            ("All Files", "*"),
            ("Python Files", "*.py,*.pyi"),
            ("HTML Files", "*.html,*.htm"),
            ("CSS Files", "*.css"),
        ),
    )

    if path != tuple():
        filePath = path

        frame = Frame(root, bg=BG, width=100, height=50)
        frame.place(x=50, y=0)
        file_name = path.split("/")
        file.config(text=f"Python IDLE- {file_name[-1]}")
        try:
            with open(filePath, "r") as data_file:
                code = data_file.read()
                code_box.delete(1.0, END)
                code_box.insert(1.0, code)
        except FileNotFoundError:
            pass


def save_file(event=NONE):
    global filePath
    if filePath == "":
        filePath = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            filetypes=(
                ("All Files", "*"),
                ("Python Files", "*.py,*.pyi"),
                ("HTML Files", "*.html,*.htm"),
                ("CSS Files", "*.css"),
            ),
        )

    with open(filePath, "w") as file:
        code = code_box.get(1.0, END)
        file.write(code)


def run_code(event=None):
    global filePath
    path = ""
    code_output.delete(1.0, END)
    if filePath == "":
        messagebox.showerror(title="Python IDLE Error", message="Save your file first")
        return
    save_file()
    for part in filePath:
        if " " in part or " \\" not in part:
            path_part = part.replace(" ", "\ ")
            path += path_part
        else:
            path = filePath
    command = f"python {path}"
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    code_output.insert(1.0, f"{command}\n\n")
    code_output.insert(END, output)
    code_output.insert(END, error)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1280x720+50+10")
    root.resizable(False, False)
    root.title("Python IDLE")
    root.config(bg=BG)
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)
    # code input
    code_box = Text(root, bg="white", highlightthickness=0, font=FONT)
    code_box.focus()
    code_box.place(x=140, y=50, height=660, width=700)
    # bindings for code box
    code_box.bind("<Control-q>", quit_app)
    code_box.bind("<Control-o>", open_file)
    code_box.bind("<Control-d>", delete_code)
    code_box.bind("<Control-r>", run_code)
    code_box.bind("<Control-s>", save_file)

    # code_output
    code_output = Text(root, bg=BG, highlightthickness=0, font=FONT, fg="lightgreen")
    code_output.place(x=850, y=50, height=660, width=400)
    # label for file name
    file = Label(
        text="Python IDLE- Untitled.py", font=("Arial", 15, "bold"), bg=BG, fg="white"
    )
    file.place(x=500, y=10)
    # add new file in idle
    add_img = PhotoImage(file="add.png")
    open_button = Button(
        root, bg=BG, image=add_img, highlightthickness=0, command=open_file
    )
    open_button.place(x=10, y=50)
    # save image and button
    save_img = PhotoImage(file="save.png")
    save_button = Button(
        root, bg=BG, image=save_img, highlightthickness=0, command=save_file
    )
    save_button.place(x=10, y=180)
    # run image and button
    run_img = PhotoImage(file="run1.png")
    run_button = Button(
        root, bg=BG, image=run_img, highlightthickness=0, command=run_code
    )
    run_button.place(x=10, y=310)
    # delete button
    del_img = PhotoImage(file="delete.png")
    del_button = Button(
        root, bg=BG, image=del_img, highlightthickness=0, command=delete_code
    )
    del_button.place(x=10, y=440)
    # quit image
    quit_img = PhotoImage(file="quit.png")
    quit_button = Button(
        root, bg=BG, image=quit_img, highlightthickness=0, command=quit_app
    )
    quit_button.place(x=10, y=570)
    root.mainloop()
