from tkinter import *
from random import choice
from tkinter import messagebox

BG = "#fcf6bd"
COLORS = ("#8cb369", "#ce4257", "#0353a4", "#0582ca", "#006daa", "#07beb8","#b5179e","#15616d","#52b788")
T_FONT = ("ARIAL", 25, "bold")
N_FONT = ("Ubuntu", 20, "normal")
H_FONT = ("ARIAL", 100, "normal")
DICE = {"\u2680": 1, "\u2681": 2, "\u2682": 3, "\u2683": 4, "\u2684": 5, "\u2685": 6}


def dice(value):
    frame = Frame(root, bg=BG, width=350, height=350)
    frame.place(x=0, y=0)
    sum = 0
    for i in range(value):
        x_position = [10, 10, 200, 200]
        y_position = [40, 180] * 2
        key, value = choice(list(DICE.items()))
        sum += value
        label = Label(frame, text=key, bg=BG, font=H_FONT, fg=choice(COLORS))
        label.place(x=x_position[i - 1], y=y_position[i - 1])
    Label(frame, text=f"Sum of dices:{sum}", bg=BG, fg=choice(COLORS), font=N_FONT).place(
        x=0, y=310
    )
def quit_app(event=None):
    if messagebox.askokcancel(title="Quit The App",message="Do you want to quit the dice roller app?"):
        root.destroy()
def roll(event=None):
    if entry.get() != "":
        value = int(entry.get())
        if 1 <= value <= 4:
            dice(value)

        else:
            label = Label(
                text="Value should be between 1 and 4.",
                fg=choice(COLORS),
                bg=BG,
                font=N_FONT,
            )
            label.place(x=00, y=500)
            entry.delete(0, END)
            root.after(1000, label.destroy)
    else:
        screen = Toplevel(root)
        screen.geometry("230x100")
        Label(
            screen,
            text="Input valid value \n for no of dices.",
            fg=choice(COLORS),
            font=N_FONT,
        ).pack()
        screen.after(1200, lambda: screen.destroy())


if __name__ == "__main__":
    root = Tk()
    root.title("DICE ROLLER")
    root.config(bg=BG, padx=50, pady=50)
    root.geometry("480x600")
    root.resizable(False, False)
    entry = Entry(
        fg=choice(COLORS), bd=0, justify="center", relief=GROOVE, width=5, font=T_FONT
    )
    entry.focus()
    entry.bind("<Control-q>",quit_app)
    entry.bind("<Return>", roll)
    entry.place(x=155, y=350)

    Button(
        text="ROLL THE DICE",
        font=T_FONT,
        fg=choice(COLORS),
        highlightthickness=0,
        command=roll,
    ).place(x=50, y=400)
    root.mainloop()

