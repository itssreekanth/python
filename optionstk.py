from tkinter import *
def selected():
	print("selected",str(var.get()))
root = Tk()
var = IntVar()
r1 = Radiobutton(root,text='option1',variable = var,value = 1,command = selected)
r1.pack(anchor = W)

r1 = Radiobutton(root,text='option2',variable = var,value = 2,command = selected)
r1.pack(anchor = W)

r1 = Radiobutton(root,text='option3',variable = var,value = '11',command = selected)
r1.pack(anchor = W)

for x in range(4,6):
	text = 'option'+str(x)
	r1 = Radiobutton(root,text=text,variable = var,value = str(x),command = selected)
	r1.pack(anchor = W)
#r1.forget()
#r1.destroy()
#print(var.get())
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
widget_list = all_children(root)
for item in widget_list:
    item.pack_forget()
label = Label(root)
label.pack()
root.mainloop()