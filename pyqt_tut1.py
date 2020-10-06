from tkinter import *

root = Tk()

w = Spinbox(root,from_=0,to=10,width=3)
def function():
    a = w.get()
    print(a)
b = Button(root,text='click',command = function)
b.pack()
def function():
    a = w.get()
    print(a)
w.pack()

mainloop()