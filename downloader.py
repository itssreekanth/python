from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image,ImageTk
from pytube import YouTube as youtube
from threading import *
from tkinter.messagebox import askyesno

filesize = 0

def downloader():
	thread = Thread(target = downloader)
	thread.start()
def progress(chunk,file_handle,remaining):
	global download_status
	file_downloaded = file_size-remaining
	per = (file_downloaded/file_size)*100
	download_status.config(text = '{:00.0f} % downloaded \n {:00.0f} mb/ {:00.0f} mb'.format(per,(int(file_downloaded)/1024)/1024,(int(file_size)/1024)/1024))

def downloader():
	global file_size, download_status
	download_btn.config(state = DISABLED)
	download_status.config(text='Please Wait...')
	download_status.place(x=230,y=250)
	try:
		url1 = url.get()
		path = askdirectory()
		yt = youtube(url1,on_progress_callback=progress)
		video = yt.streams.filter(progressive = True, file_extension = 'mp4').first()
		#print(yt.streams.filter(progressive = True, file_extension = 'mp4'))

		file_size = video.filesize
		video.download(path)
		download_status.config(text = 'Download Finish...')
		res = askyesno("Youtube Video Downloader","Do you want to download another video?")
		if res ==1:
			url.delete(0,END)
			download_btn.config(state=NORMAL)
			download_status.config(text=" ")
		else:
			root.destroy()
	except Exception as e:
		download_status.config(text='Failed! An error occured.')
		download_btn.config(state=NORMAL)
		#download_status.config(text=" ")
		url.delete(0,END)


root = Tk()
root.geometry('600x400')
#root.iconbitmap('logo.ico')
root.title("Youtube Video Downloader")
root['bg'] = 'white'
root.resizable(0,0)

#img = Image.open('logo.ico')
#img = img.resize((80,80),Image.ANTIALIAS)
#img = ImageTk.PhotoImage(img)
#head = Label(root, image = img)
#head.config(anchor = CENTER)
#head.pack()

enter_url = Label(root,text = 'Enter URL : ',bg = 'white')
enter_url.config(font=('Verdana',15))
enter_url.place(x=5,y=120)

url = Entry(root, width = 35, border = 1, relief = SUNKEN, font = ('Verdana',15))
url.place(x=125,y=123)

download_btn_img = Image.open('download_button.png')
download_btn_img = download_btn_img.resize((200,50),Image.ANTIALIAS)
download_btn_img = ImageTk.PhotoImage(download_btn_img)

download_btn = Button(root, width =200, height = 50, bg = 'white', relief=FLAT,activebackground='black',command = downloader)
download_btn.config(image = download_btn_img)
download_btn.place(x = 220,y = 170)

download_status = Label(root,text = 'Please Wait...',font = ('Verdana',15),bg = 'white')
root.mainloop()

