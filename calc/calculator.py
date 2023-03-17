import tkinter
from tkinter import *
BG_COLOR="#17161b"
FONT=("Arial",30,"bold")
BUTTON_BG="#2a2d36"
FG="#FFF"
X=[10,160,310,460]
Y=120
Y_DIFF=90
BUTTON_TEXT=["C","/","%","*","9","8","7","-","6","5","4","+","3","2","1","0",".","="]
SYMBOLS=["/","%","*","-","+","."]
# -------------------------CALCULATOR FUNCTION---------------------------------------------#
equation=""
result=""


def solution():
    global equation,result
    if equation!="":
        try:
            result=eval(equation)
        except ZeroDivisionError:
            result="Cannot be divided by zero"
        except SyntaxError:
            result="Use signs properly."
        equation=""
        result_label.config(text=result)
def show(value):
    global equation,result
    if result:
        equation=str(result)
        result=""
    equation+=value
    result_label.config(text=equation)

def clear():
    global equation,result
    equation=""
    result=""
    result_label.config(text=equation)
# -------------------------------------------------------UI SETUP------------------------------------------------------------------#
root=Tk()
root.title("Simple GUI Calculator")
root.geometry('600x570+100+200')
root.resizable(False,False)
root.config(bg=BG_COLOR)


result_label=Label(root,text="",width=26,height=2,font=FONT,bg="white")
result_label.pack()

# ---------------FIRST ROW---------------------#
Button(root,text=BUTTON_TEXT[0],width=5,height=1,bd=1,font=FONT,fg=FG,bg="#3697f5",command=lambda:clear()).place(x=X[0],y=Y)
Button(root,text=BUTTON_TEXT[1],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[1])).place(x=X[1],y=Y)
Button(root,text=BUTTON_TEXT[2],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[2])).place(x=X[2],y=Y)
Button(root,text=BUTTON_TEXT[3],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[3])).place(x=X[3],y=Y)

# ----------------SEC0ND ROW----------------------#
Button(root,text=BUTTON_TEXT[4],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[4])).place(x=X[0],y=Y+Y_DIFF)
Button(root,text=BUTTON_TEXT[5],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[5])).place(x=X[1],y=Y+Y_DIFF)
Button(root,text=BUTTON_TEXT[6],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[6])).place(x=X[2],y=Y+Y_DIFF)
Button(root,text=BUTTON_TEXT[7],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[7])).place(x=X[3],y=Y+Y_DIFF)

# ----------------THIRD ROW----------------------#
Button(root,text=BUTTON_TEXT[8],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[8])).place(x=X[0],y=Y+2*Y_DIFF)
Button(root,text=BUTTON_TEXT[9],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[9])).place(x=X[1],y=Y+2*Y_DIFF)
Button(root,text=BUTTON_TEXT[10],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[10])).place(x=X[2],y=Y+2*Y_DIFF)
Button(root,text=BUTTON_TEXT[11],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[11])).place(x=X[3],y=Y+2*Y_DIFF)

# -----------------FOURTH ROW--------------------#
Button(root,text=BUTTON_TEXT[12],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[12])).place(x=X[0],y=Y+3*Y_DIFF)
Button(root,text=BUTTON_TEXT[13],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[13])).place(x=X[1],y=Y+3*Y_DIFF)
Button(root,text=BUTTON_TEXT[14],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[14])).place(x=X[2],y=Y+3*Y_DIFF)

# -----------------FIFTH ROW--------------------#
Button(root,text=BUTTON_TEXT[15],width=11,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[15])).place(x=X[0],y=Y+4*Y_DIFF)
Button(root,text=BUTTON_TEXT[16],width=5,height=1,bd=1,font=FONT,fg=FG,bg=BUTTON_BG,command=lambda:show(BUTTON_TEXT[16])).place(x=X[2],y=Y+4*Y_DIFF)
Button(root,text=BUTTON_TEXT[17],width=5,height=3,bd=1,font=FONT,fg=FG,bg="#FE9037",command=solution).place(x=X[3],y=Y+3*Y_DIFF)



root.mainloop()