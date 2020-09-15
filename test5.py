from tkinter import *
from PIL import Image,ImageTk
class app():
	def __init__(self):
		self.root = Tk()
		self.root.geometry('600x400')
		self.home()
		self.root.mainloop()
	def home(self):
		self.enter_url = Button(self.root,text = 'Enter URL : ',font=('Verdana',14),command=self.downloader1)
		self.enter_url.place(x=5,y=150)
		
	def downloader1(self):
		self.enter_url.destroy()
		self.download_btn_img = Image.open('download_button.png')
		self.download_btn_img = self.download_btn_img.resize((200,50),Image.ANTIALIAS)
		self.download_btn_img = ImageTk.PhotoImage(self.download_btn_img)
		self.download_btn = Button(self.root, width =200, height = 50, relief=FLAT,activebackground='black',image = self.download_btn_img,command=self.downloader)
		self.download_btn.place(x = 195,y = 320)
	def downloader(self):
		def all_children (window) :
			print('yes')
			_list = window.winfo_children()
			print(_list)
			for item in _list :
				if item.winfo_children() :
					_list.extend(item.winfo_children())
			return _list
		widget_list = all_children(self.root)
		for item in widget_list:
		    item.destroy()
		    print('cleared')
a = app()