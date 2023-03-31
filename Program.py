from tkinter import *
import tkinter.messagebox
#monitor1
root = Tk()
root.title("My GUI")
#screen size
root.geometry("450x350+600+500")

def showChoice():
    choice=language.get()
    if choice == 1:
        tkinter.messagebox.showinfo("warning","you have selected Python")
    elif choice == 2:
        tkinter.messagebox.showinfo("warning","you have selected Java")
    elif choice == 3:
          tkinter.messagebox.showinfo("warning","you have selected PHP")
    else:
          tkinter.messagebox.showinfo("warning","you have selected c#")
   
  

#option
language = IntVar()
language.set(2)
Radiobutton(text="Python",variable=language,value=1,command=showChoice).grid(row=0,column=0)
Radiobutton(text="Java",variable=language,value=2,command=showChoice).grid(row=0,column=1)
Radiobutton(text="PHP",variable=language,value=3,command=showChoice).grid(row=0,column=2)
Radiobutton(text="c#",variable=language,value=4,command=showChoice).grid(row=0,column=3)





root.mainloop()




