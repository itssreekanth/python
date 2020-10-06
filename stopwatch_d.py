from tkinter import *
import time,os,notify2
from PyQt5 import QtCore
from threading import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class stop_watch():
	def __init__(self):
		self.running = False
		self.count=66600
		self.root = Tk()
		self.root.title("StopWatch")
		self.root.geometry('300x260')
		self.d_time="00:00:00"
		self.timer_label = Label(self.root,text='Set timer : ',font = ('1',12))
		self.timer_label.grid(row=0,column=0,padx=11)
		self.hour_box = Spinbox(self.root,from_=0,to=24,width=2)
		self.hour_box.grid(row=0,column=1,pady=19)
		self.hour_label = Label(self.root,text=' H ')
		self.hour_label.grid(row=0,column=2)
		self.minute_box = Spinbox(self.root,from_=0,to=60,width=2)
		self.minute_box.grid(row=0,column=3)
		self.minute_label = Label(self.root,text=' M ')
		self.minute_label.grid(row=0,column=4)
		self.second_box = Spinbox(self.root,from_=0,to=60,width=2)
		self.second_box.grid(row=0,column=5)
		self.second_label = Label(self.root,text=' S')
		self.second_label.grid(row=0,column=6)
		self.repeat_label = Label(self.root,text='Repeat    :',font=('1',12))
		self.repeat_label.grid(row=1,column=0)
		self.repeat_box = Spinbox(self.root,from_=0,to=100,width=5)
		self.repeat_box.grid(row=1,column=1,columnspan=2)
		self.label = Label(self.root,text = '   Welcome!',font=('1',19))
		self.label.grid(row=2,column=0,columnspan=7,pady=30)
		self.start = Button(self.root,text = 'Start',width = 6,command = self.Start)
		self.stop = Button(self.root,text = 'Stop',width = 6, state = 'disabled',command = self.stop)
		self.reset = Button(self.root,text = 'Reset',width=6, state = 'disabled',command=self.Reset)
		self.start.grid(row=3,column=0,columnspan=2)
		self.stop.grid(row=3,column=1,columnspan=3)
		self.reset.grid(row=3,column=4,columnspan=4)
		self.empty = Label(self.root,text='')
		self.empty.grid(row = 4,column=0)
		self.minimize = Button(self.root,text='Hide',width=7,command=self.tray)
		self.minimize.grid(row=4,column=1,columnspan=3,pady=8)
		self.root.mainloop()
	def router(self):
		tray_thread = Thread(target=self.tray)
		#timer_thread = Thread(target=self.counter)
		tray_thread.start()
		#timer_thread.start()
	def tray(self):
		self.root.withdraw()
		app = QApplication([])
		app.setQuitOnLastWindowClosed(False)

		def timerEvent():
			global ttime
			#ttime = ttime.addSecs(1)
			#print(self.d_time)
			realtime = time.ctime(self.count)
			realtime = realtime.split(" ")
			watch = realtime[4]
			option1.setText(watch)
			self.count+=1

		icon = QIcon('icon.png')
		tray = QSystemTrayIcon()
		tray.setIcon(icon)
		tray.setVisible(True)

		menu = QMenu()
		#self.counter()
		option1 = QAction("00:00:00")
		option2 = QAction('Notification ON')

		menu.addAction(option1)
		menu.addAction(option2)

		option1.triggered.connect(self.call_back)
		option1.triggered.connect(app.quit)

		quit = QAction('quit')
		quit.triggered.connect(self.collapse)
		menu.addAction(quit)
		quit.triggered.connect(app.quit)
		tray.setContextMenu(menu)
		#tray_time=QtCore.QTime(0,0,0)
		if self.running:
			timer = QtCore.QTimer()
			ttime = QtCore.QTime(0,0,0)
			timer.timeout.connect(timerEvent)
			timer.start(1000)
		else:
			option1.setText(self.d_time)
		app.exec_()
	def call_back(self):
		self.root.deiconify()
	def collapse(self):
		self.root.destroy()
	def counter(self):
		def sound():
			show_timer = 'Timer : '+self.d_time
			notify2.init('')
			n = notify2.Notification('Stopwatch',show_timer,'notification-message-im')
			n.show()
			os.system('play -nq -t alsa synth {} sine {}'.format(1,5000))
			if str(self.repeat)=='True':
				self.timer+=self.x_timer-66600
			elif self.repeat>1:
				self.timer+=self.x_timer-66600
				self.repeat-=1
			coun()
		def coun():
			if self.running:
				if self.count==66600:
					display='   00:00:00'
				else:
					realtime = time.ctime(self.count)
					realtime = realtime.split(" ")
					self.d_time = realtime[4]
					display = "   "+self.d_time
					#print(display)
				self.label['text'] = display
				#print(self.timer,self.count)
				if self.count==self.timer:
					thread = Thread(target=sound)
					thread.start()
				else:
					self.label.after(1000,coun)
				self.count+=1
		coun()

	def Start(self):
		self.running = True
		self.start['state'] = 'disabled'
		self.stop['state'] = 'normal'
		self.reset['state'] = 'normal'
		self.hour_box['state']='disabled'
		self.minute_box['state']='disabled'
		self.second_box['state']='disabled'
		self.repeat_box['state']='disabled'
		self.reset['command']=self.Reset
		hour = self.hour_box.get()
		minute = self.minute_box.get()
		seconds = self.second_box.get()
		repeat = self.repeat_box.get()
		if hour:
			hour=int(hour)
		else:
			hour = 0
		if minute:
			minute = int(minute)
		else:
			minute=0
		if seconds:
			seconds=int(seconds)
		else:
			seconds=0
		if repeat:
			self.repeat=int(repeat)
		else:
			self.repeat=1
		self.timer = ((hour*3600)+(minute*60)+seconds)
		if self.timer==0:
			self.repeat=False
		else:
			self.timer+=66600
		self.x_timer = self.timer
		self.x_repeat = self.repeat
		self.counter()
	def stop(self):
		self.start['state'] = 'normal'
		self.stop['state'] = 'disabled'
		self.reset['state'] = 'normal'
		self.running = False
	def Reset(self):
		self.count = 66600
		if self.running==False:
			self.reset['command'] = self.timer_reset
		self.label['text'] = '   00:00:00'
	def timer_start(self):
		
		
		a=self.hour_box.get()
		#print(type(a))
		
	def timer_reset(self):
		self.hour_box['state']='normal'
		self.minute_box['state']='normal'
		self.second_box['state']='normal'
		self.repeat_box['state']='normal'
		self.hour_box.delete(0,2)
		self.minute_box.delete(0,2)
		self.second_box.delete(0,2)
		self.repeat_box.delete(0,2)
stop_watch()