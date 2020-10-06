import tkinter
from tkinter import *
window = Tk()

#w = tk.Label(root, text="red", bg="red", fg="white")
#w.pack(padx=5, pady=10, side=tk.LEFT)
name = tkinter.Label(window, text="Name : ", fg="black")
name.grid(row=0, column=1,columnspan=2)
nametext = tkinter.Entry(window,width=23)
nametext.grid(row=0, column=3,columnspan=2)
age = tkinter.Label(window, text="Age : ")
age.grid(row=1, column=1 ,columnspan=2)
agetext = tkinter.Entry(window, width=23)
agetext.grid(row=1, column=3 ,columnspan=2)
confidencel = tkinter.Label(window, text="Confidence : ")
confidencel.grid(row=2, column=1 ,columnspan=2)
confidenceltext = tkinter.Entry(window, width=23)
confidenceltext.grid(row=2, column=3 ,columnspan=2)
def ca():
	window.iconify()
def wo():
	window.withdraw()
	ca()
new = tkinter.Button(window, text="new", bg="orange", fg="black",command = wo)
new.grid(row=3, column=2 )
btn_snapshot = tkinter.Button(window, text="capture", bg="skyblue", fg="black")
btn_snapshot.grid(row=3, column=4 )
nametext.insert(0, "a default value")
btn_snapshot.destroy()




s = nametext.get()
print(s)
nametext.delete(0,END)
#mresult = tkinter.Label(window, textvariable = nametext)
#mresult.pack()
#w = tk.Label(root, text="blue", bg="blue", fg="white")
#w.pack(padx=5, pady=20, side=tk.LEFT)

tkinter.mainloop()

