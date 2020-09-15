from pytube import YouTube as youtube
from tkinter import *
from pytube import Playlist
class app():
	def __init__(self):
		self.root = Tk()
		self.root.geometry('600x480')
		self.next = Button(self.root, text="Next", bg="orange", fg="black",command=self.download)
		self.next.place(x=350,y=220)
		
		self.download_status = Label(self.root,text = 'Downloading...',font=('Verdana',15))
		self.download_status.place(x=0,y=50)
		self.root.mainloop()

	def progress(self,chunk,file_handle,remaining):
		file_downloaded = self.file_size-remaining
		per = (file_downloaded/self.file_size)*100
		self.download_status.config(text='{:00.0f} % downloaded \n {:00.0f} mb/ {:00.0f} mb'.format(per,(int(file_downloaded)/1024)/1024,(int(self.file_size)/1024)/1024))
	def download(self):
		video = youtube('https://youtu.be/YV0C22shXMk',on_progress_callback=self.progress).streams
		#print(video)
		a = video.filter(progressive=True).first()

		#print(video.filter(subtype='mp4').res())

		a = video.filter(only_audio=True).first()
		self.file_size = a.filesize
		print(a)
		a.download()
		#print(video.filter(adaptive=True,type='video',subtype='mp4'))
		'''for x in a:
									print(x.abr)'''

#app()
pl = Playlist("https://www.youtube.com/playlist?list=PLjEaoINr3zgEq0u2MzVgAaHEBt--xLB6U")
pl.download('/home/sreekanth/Videos')