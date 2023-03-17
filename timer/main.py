from datetime import datetime
from tkinter import *

# from playsound import playsound
import time
from tkinter import messagebox

BG = "black"
H_FONT = ("Arial", 22, "bold")
T_FONT = ("Ubuntu", 15, "bold")
E_FONT = ("Ubuntu", 35, "bold")
time_value = 0


def show_clock():
    clock_time = time.strftime("%H:%M:%S %p")
    current_time_label.config(text=clock_time)
    current_time_label.after(1000, show_clock)


def quit_app():
    if messagebox.askokcancel(
        title="Quit The Timer", message="Do you want to quit the timer app?"
    ):
        root.after_cancel(current_time_label)
        root.destroy()


def reset_time():
    hrs.set("00")
    mins.set("00")
    secs.set("00")


def format_value(value, time_value):
    time_value.set("0" + str(value))


def start_timer():
    global time_value
    time_value = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(secs.get())
    print(time_value)
    while time_value > 0:
        minute, second = (time_value // 60, time_value % 60)
        hour = 0
        if minute >60:
            hour, minute = (time_value // 60, time_value % 60)
        hrs.set(hour)
        mins.set(minute)
        secs.set(second)
        if hour < 10:
            format_value(hour, hrs)
        if minute < 10:
            format_value(minute, mins)
        if second < 10:
            format_value(second, secs)
        root.update()
        time.sleep(1)
        time_value -= 1

    if time_value == 0:
        reset_time()


def stop_timer():
    global time_value
    time_value = -1


if __name__ == "__main__":
    root = Tk()
    root.title("TIMER APP")
    root.resizable(False, False)
    root.geometry("400x600")
    root.config(bg=BG, padx=50)
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)
    # timer heading
    heading = Label(text="Timer", font=H_FONT, fg="#ea3548", bg=BG)
    heading.pack(pady=10)
    # current time clock
    Label(root, text="Current time:", bg=BG, fg="papaya whip", font=T_FONT).pack()
    current_time_label = Label(root, font=T_FONT, bg="white", fg=BG, text="")
    current_time_label.pack()
    show_clock()

    # hour value
    hrs = StringVar(value="00")
    Entry(root, text=hrs, width=2, font=E_FONT, bg=BG, fg="white", bd=0).place(
        x=10, y=175, height=50
    )
    # minutes value
    mins = StringVar(value="00")
    Entry(root, text=mins, width=2, font=E_FONT, bg=BG, fg="white", bd=0).place(
        x=130, y=175, height=50
    )
    # seconds value
    secs = StringVar(value="00")
    Entry(root, text=secs, width=2, font=E_FONT, bg=BG, fg="white", bd=0).place(
        x=250, y=175, height=50
    )
    # creates : between above entries
    for i in range(90, 240, 125):
        Label(root, text=":", font=E_FONT, fg="white", bg="black").place(x=i, y=170)
    # start button
    start_button = Button(
        text="START",
        font=T_FONT,
        fg="white",
        bg="#3f7d20",
        highlightthickness=0,
        command=start_timer,
    )
    start_button.place(x=10, y=500)
    # stop button
    stop_button = Button(
        text="STOP",
        font=T_FONT,
        fg="white",
        bg="#43bccd",
        highlightthickness=0,
        command=stop_timer,
    )
    stop_button.place(x=130, y=500)
    # reset button
    reset_button = Button(
        text="RESET",
        font=T_FONT,
        fg="white",
        bg="#ea3546",
        highlightthickness=0,
        command=reset_time,
    )
    reset_button.place(x=250, y=500)
    # quit button
    quit_button = Button(
        text="QUIT",
        font=T_FONT,
        fg="white",
        bg="#8d0801",
        highlightthickness=0,
        command=quit_app,
    )
    quit_button.place(x=130, y=560)

    root.mainloop()
