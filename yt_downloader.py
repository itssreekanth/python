from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image,ImageTk
from pytube import YouTube as youtube
from tkinter.messagebox import askyesno
import time
from threading import *
class app:
	def __init__(self):
		self.root = Tk()
		self.root.title("Youtube video Downloader")
		self.root.geometry('600x400')
		self.var = IntVar()
		#self.text = Label(self.root,text="Welcome!",font=('Verdana',12))
		#self.text.grid(row=0,column=3)
		self.download_status = Label(self.root,text = '',font=('Verdana',15))
		self.download_status.place(x=170,y=80)
		self.home()
		self.root.mainloop()
	def home(self):
		self.enter_url = Label(self.root,text = 'Enter URL : ',font=('Verdana',14))
		self.enter_url.place(x=5,y=150)
		self.welcome = Label(self.root,text = 'Welcome to youtube downloader',font=('Verdana',14))
		#self.welcome.place(x=140,y=100)
		self.url = Entry(self.root, width = 35, border = 1, relief = SUNKEN, font = ('Verdana',15))
		self.url.place(x=125,y=150)
		self.clear = Button(self.root, text="Clear", bg="skyblue", fg="black",command = self.clear_cmd)
		self.clear.place(x=200,y=220)
		self.next = Button(self.root, text="Next", bg="orange", fg="black",command=self.resolution)
		self.next.place(x=350,y=220)
	def clear_cmd(self):
		self.url.delete(0,END)
		self.download_status.config(text='')
	def down_thread(self):
		thread = Thread(target = self.downloader)
		thread.start()
	def progress(self,chunk,file_handle,remaining):
		self.file_downloaded = self.file_size-remaining
		self.per = (self.file_downloaded/self.file_size)*100
		self.download_status.config(text = '{:00.0f} % downloaded \n {:00.0f} mb/ {:00.0f} mb'.format(self.per,(int(self.file_downloaded)/1024)/1024,(int(self.file_size)/1024)/1024))
	def resolution(self):
		try:
			url1 = self.url.get()
			self.yt = youtube(url1,on_progress_callback=self.progress).streams
			self.audiovideo = self.yt.filter(progressive=True)
			y_axis=200
			x=0
			for y in self.audiovideo:
				res = y.resolution
				itag = y.itag
				self.av1 = Radiobutton(self.root,text=res,variable = self.var,value = itag)
				self.av1.place(x=115,y=y_axis)
				y_axis+=30
				x+=1
				if x==5:
					break

			self.videoonly = self.yt.filter(adaptive=True,type='video',subtype='mp4')
			y_axis=200
			x=0
			for y in self.videoonly:
				res = y.resolution
				itag = y.itag
				self.video1 = Radiobutton(self.root,text=res,variable = self.var,value = itag)
				self.video1.place(x=270,y=y_axis)
				y_axis+=30
				x+=1
				if x==5:
					break
			y_axis=200
			self.audioonly = self.yt.filter(only_audio = True)
			x=0
			for y in self.audioonly:
				res = y.abr
				itag = y.itag
				self.audio1 = Radiobutton(self.root,text=res,variable = self.var,value = itag)
				self.audio1.place(x=420,y=y_axis)
				y_axis+=30
				x+=1
				if x==5:
					break
			self.enter_url.destroy()
			self.url.destroy()
			self.clear.destroy()
			self.next.destroy()
			self.download_btn_img = Image.open('download_button.png')
			self.download_btn_img = self.download_btn_img.resize((200,50),Image.ANTIALIAS)
			self.download_btn_img = ImageTk.PhotoImage(self.download_btn_img)
			self.download_btn = Button(self.root, width =200, height = 50, relief=FLAT,activebackground='black',image = self.download_btn_img,command=self.down_thread)
			self.download_btn.place(x = 195,y = 320)
			self.download_status = Label(self.root,text = 'Select the resolution for the video',font=('Verdana',15))
			self.download_status.place(x=140,y=50)
			

			self.av = Label(self.root,text = 'Video+Audio')
			self.av.place(x=110,y=170)
			self.video = Label(self.root,text = 'Only Video')
			self.video.place(x=273,y=170)
			self.audio = Label(self.root,text = 'Only Audio')
			self.audio.place(x=430,y=170)
		except Exception as e:
			self.download_status.config(text = 'Error Occured! Try agian.')
			self.home()
	def downloader(self):
		try:
			self.path = askdirectory()
			def all_children (window) :
				print('yes')
				_list = window.winfo_children()
				for item in _list :
					if item.winfo_children() :
						_list.extend(item.winfo_children())
				return _list
			widget_list = all_children(self.root)
			for item in widget_list:
			    item.destroy()

			
			self.download_status=Label(self.root,text = 'Downloading...',font = ('Verdana',15))
			self.download_status.place(x=210,y=190)
			tag = self.var.get()
			self.yt1 = self.yt.get_by_itag(tag)
			self.file_size = self.yt1.filesize
			self.yt1.download(self.path)
			self.download_status.config(text = 'Download Finished...',font = ('Verdana',15))
			self.download_status.place(x=200,y=50)
			self.home()
		except Exception as e:
			self.download_status.config(text = 'Error Occured! Try agian.')
			self.home()
app()
