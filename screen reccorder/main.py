from tkinter import *
import pyscreeze


if __name__=="__main__":
    root=Tk()
    root.title("Screen Recorder App")
    root.geometry("400x600+400+100")
    root.resizable(False,False)
    icon=PhotoImage(file="video.png")
    root.iconphoto(False,icon)


    root.mainloop()