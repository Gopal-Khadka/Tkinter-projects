from email import message
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

BG = "lightblue"
BG_BTN = "#fff"


def saveFile():
    save_file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if not save_file:
        return
    data = str(text.get(1.0, END))
    save_file.write(data)
    save_file.close()


def openFile():
    open_file = filedialog.askopenfile(mode="r", filetypes=[("text files", "*.txt")])
    data=str(text.get(1.0, END))
    if len(data)!=1:
        if messagebox.askokcancel(title="Clear the contents",message="Do you want to clear contents of textbox?"):
            text.delete(1.0,END)
        else:
            saveFile()
    content = open_file.read()
    text.insert(INSERT, content)


def exitApp():
    if messagebox.askokcancel(
        title="Exit The App", message="Do you want to exit the notepad?"
    ):
        root.destroy()


# ------------------------------------------UI SETUP----------------------------------#
root = Tk()
root.title("GUI Notepad")
root.geometry("580x600")
root.resizable(False, False)
root.config(bg=BG)

# save button
save_btn = Button(
    root, width=15, height=1, text="Save File", bg=BG_BTN, command=saveFile
)
save_btn.grid(row=0, column=0)
# open button
open_btn = Button(
    root, width=15, height=1, text="Open File", bg=BG_BTN, command=openFile
)
open_btn.grid(row=0, column=1)
# close button
open_btn = Button(root, width=15, height=1, text="Exit App", bg=BG_BTN, command=exitApp)
open_btn.grid(row=0, column=2)
# text box
text = Text(root, width=70, height=33, padx=1, pady=1)
text.grid(row=1, column=0, columnspan=3)


root.mainloop()
