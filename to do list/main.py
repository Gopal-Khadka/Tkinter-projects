from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("TO DO LIST APP")
root.geometry("400x700+400+100")
root.resizable(False, False)
root.config(bg="white")
TASK_LIST = []
BG = "#32405b"
WHITE = "white"
FONT = ("Arial", 20, "bold")


# adds task when add button is pressed
def addTask(event=None):
    global TASK_LIST
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("task.txt","a") as tasks:
            tasks.writelines(f"{task}\n")
        TASK_LIST.append(task)
        listbox.insert(0,task)
        
# open data file and retrieve todo tasks
def openTaskFile():
    global TASK_LIST
    try:
        with open("task.txt") as taskfile:
            tasks = taskfile.readlines()
    except FileNotFoundError:
        with open("task.txt", "w") as taskfile:
            listbox.insert(END, "No datafile found")
    else:
        for task in tasks:
            if task != "\n":
                task = task.replace("\n", "")
                TASK_LIST.append(task)
                listbox.insert(0, task)


# delete task from file when delete button is pressed
def deleteTask(event=None):
    global TASK_LIST
    task=listbox.get(ANCHOR)
    delete=messagebox.askokcancel(title="Delete data",message="Do you want to delete this data?")
    if delete and task in TASK_LIST:
        TASK_LIST.remove(task)
        with open("task.txt","w") as tasks:
            for task in TASK_LIST:
                tasks.write(f"{task}\n")
        listbox.delete(ANCHOR)



# ----------------UI SETUP---------------#

# task icon
task_icon = PhotoImage(file="task.png")
root.iconphoto(True, task_icon)

# top bar
topbar = PhotoImage(file="topbar.png")
Label(root, image=topbar, bg=WHITE).pack()

# dock image
dockimg = PhotoImage(file="dock.png")
Label(root, image=dockimg, bg=BG).place(x=30, y=25)
# note image
noteimg = PhotoImage(file="task.png")
Label(root, image=noteimg, bg=BG).place(x=340, y=25)
# heading
heading = Label(root, text="ALL TASK", bg=BG, fg=WHITE, font=FONT)
heading.place(x=130, y=20)

# frame
frame = Frame(root, width=400, height=50, bg=WHITE)
frame.place(x=0, y=180)
# task entry
task = StringVar()
task_entry = Entry(frame, bd=0, width=25, font=("Ubuntu", 15))
task_entry.focus()
task_entry.bind("<Return>",addTask)
task_entry.place(x=10, y=7)
# add buttton
add_btn = Button(frame, text="ADD", width=5, font=FONT, bd=0, bg="#5a995f", fg="#fff",command=addTask)
add_btn.place(x=300)

# list box
frame1 = Frame(root, bd=3, width=400, height=240, bg=WHITE)
frame1.pack(pady=(138, 0))

listbox = Listbox(
    frame1, font=FONT, width=25, height=13, bg=BG, fg=WHITE, selectbackground="#5a95ff"
)
listbox.pack(side=LEFT, fill=BOTH)
listbox.bind("<Return>",deleteTask)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# delete button
delete = PhotoImage(file="delete.png")
Button(root, image=delete, bd=0, highlightthickness=0, bg=WHITE,command=deleteTask).place(x=170,y=650)
exit_btn=Button(root,text="Exit",font=FONT ,bd=0, highlightthickness=0,fg="red", bg=WHITE,command=root.destroy)
exit_btn.place(x=310,y=650)
# ------------OPEN TO DOs from data file-----------------#
openTaskFile()


root.mainloop()














