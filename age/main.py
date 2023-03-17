from tkinter import *
from datetime import date, datetime,timedelta
from tkinter import messagebox
BG="#7fc8f8"
FONT=("Arial",15,"normal")
E_BG="#98c1d9"

def calc_age(event=None):
    frame=Frame(bg=BG,width=400,height=40)
    frame.place(x=0,y=550)
    try:
        today=date.today()
        birthDate=date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get()))
        age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
        Label(frame,text=F"{name_entry.get().title()},your age is {age}.",bg=BG,fg="#274c77",font=FONT).place(x=75)
    except ValueError:
        messagebox.showinfo(title="Enter valid data",message="You are requested to use valid data.")




if __name__=="__main__":
    root=Tk()
    root.title("Age Calculator")
    root.geometry("400x600+400+100")
    root.resizable(True,True)
    root.config(bg=BG)
    icon=PhotoImage(file="icon.png")
    root.iconphoto(False,icon)
    Label(root,image=icon,bg=BG).pack(pady=50)
    for i in range(4):
        x,y=70,115
        label_list=["Name","Year","Month","Day"]
        Label(root,text=label_list[i],bg=BG,font=FONT,fg="#001c55").place(x=x,y=y+(i+1)*x)
    name_entry=Entry(font=FONT,textvariable="",bg=E_BG)
    name_entry.place(x=140,y=185)
    name_entry.focus()
    year_entry=Entry(font=FONT,textvariable="",bg=E_BG)
    year_entry.place(x=140,y=255)
    month_entry=Entry(font=FONT,textvariable="",bg=E_BG)
    month_entry.place(x=140,y=325)
    day_entry=Entry(font=FONT,textvariable="",bg=E_BG)
    day_entry.place(x=140,y=395)
    day_entry.bind("<Return>",calc_age)
    Button(text="Calculate Age",bg=BG,fg="#274c77",font=FONT,highlightthickness=0,command=calc_age).place(x=120,y=475)


    root.mainloop()