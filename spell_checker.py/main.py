from tkinter import *
from textblob import TextBlob
H_FONT=("Trebuchet MS",30,"bold")
T_FONT=("Poppins",20,"normal")
B_FONT=("Arial",20,"bold")

def check_word():
    text=str(word.get())
    txt=TextBlob(text)
    right=txt.correct()
    spell.config(text=f"Correct spelling of {text}:")
    cs=Label(root,text=f"{right}",font=T_FONT,fg="blue",bg="#dae6f6")
    cs.grid(row=4,column=1)


root=Tk()
root.title("Spell Checker App")
root.geometry("700x400")
root.resizable(False,False)
root.config(bg="#dae6f6")

heading=Label(root,text="SPELL CHECKER",font=H_FONT,bg="#dae6f6",fg="#364971")
heading.grid(row=0,column=0,pady=(50,0),columnspan=2)

word=Entry(root,font=T_FONT,justify="center",bg= "#dae6f6",width=35)
word.focus()
word.grid(row=1,column=0,columnspan=2,padx=10)

button=Button(root,text="Check",command=check_word,font=B_FONT,fg="white",bg="red")
button.grid(row=3,column=0,columnspan=2,pady=20)

spell=Label(root,text="",font=T_FONT,fg="blue",bg="#dae6f6")
spell.grid(row=4,column=0)

root.mainloop()
