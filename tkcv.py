import tkinter
import cv2,pyautogui
import PIL.Image, PIL.ImageTk
import time,os,shutil
import numpy as np
from tkinter import END
from PIL import Image

class App:
	def __init__(self, window, window_title,subjects,video_source=0):
		self.window = window
		self.window.title(window_title)
		self.video_source = video_source
		self.subjects = subjects
		self.vid = MyVideoCapture()
		self.canvas = tkinter.Canvas(window, width = 380, height = 350)
		self.canvas.grid(row=0, column=0,columnspan=1,rowspan = 5,padx = 5 ,pady = 5)
		self.name = tkinter.Label(window, text="Name : ", fg="black")
		self.name.grid(row=0, column=1,columnspan=2)
		self.nametext = tkinter.Entry(window,width=23)
		self.nametext.grid(row=0, column=3,columnspan=2)
		self.age = tkinter.Label(window, text="Age : ")
		self.age.grid(row=1, column=1 ,columnspan=2)
		self.agetext = tkinter.Entry(window, width=23)
		self.agetext.grid(row=1, column=3 ,columnspan=2)
		self.confidencel = tkinter.Label(window, text="Confidence : ")
		self.confidencel.grid(row=2, column=1 ,columnspan=2)
		self.confidenceltext = tkinter.Entry(window, width=23)
		self.confidenceltext.grid(row=2, column=3 ,columnspan=2)
		self.new = tkinter.Button(window, text="New Data", bg="orange", fg="black",command = self.new_data)
		self.new.grid(row=4, column=2 )
		self.btn_snapshot = tkinter.Button(window, text="capture", bg="skyblue", fg="black", command=self.snapshot)
		self.btn_snapshot.grid(row=4, column=4 )
		self.labeltext = tkinter.Label(window, text="Click on New Data to register face\n\n Click on Capture to take a picture")
		self.labeltext.grid(row=3,column=1,columnspan=5)
		self.count = 1
		self.labeltime = 1
		self.acces = 0
		self.waittime = 0
		self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
		self.training()
		self.delay = 15

		self.update()
		self.window.mainloop()
	def snapshot(self):

		ret, frame = self.vid.get_frame()
		if ret:
			cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
			self.labeltext["text"] = "Captured"
			self.labeltime = time.time()
			self.labeltime+=2
	def detect_face(self,img):
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
		if (len(faces) == 0):
			return None, np.zeros(4)
		(x, y, w, h) = faces[0]
		return gray[y:y+w, x:x+h], faces[0]
	def prepare_training_data(self,data_folder_path):
		dirs = os.listdir(data_folder_path)
		faces = []
		labels = []
		for dir_name in dirs:
			if not dir_name.startswith("s"):
				continue;
			label = int(dir_name.replace("s", ""))
			subject_dir_path = data_folder_path + "/" + dir_name
			subject_images_names = os.listdir(subject_dir_path)
			for image_name in subject_images_names:
				if image_name.startswith("."):
					continue;
				image_path = subject_dir_path + "/" + image_name
				image = cv2.imread(image_path)
				#cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
				#cv2.waitkey(100)
				face, rect = self.detect_face(image)
				if face is not None:
					faces.append(face)
					labels.append(label)
		#cv2.destroyAllWindows()
		#cv2.waitKey(1)
		#cv2.destroyAllWindows()
		return faces, labels
	def training(self):
		print("Preparing data...")
		faces, labels = self.prepare_training_data("train")
		print("Data prepared")
		print("Total faces: ", len(faces))
		#print("Total labels: ", len(labels))
		self.face_recognizer.train(faces, np.array(labels))
	def frame(self):
		if self.labeltime<=time.time()<=self.labeltime+0.8:
			self.labeltext["text"] = "Click on New Data to register face\n\n Click on Capture to take a picture"
		ret, frame = self.vid.get_frame()
		if ret:
			img = frame.copy()
			face, rect = self.detect_face(img)
			if rect.any() != 0:
				label,confidence = self.face_recognizer.predict(face)
				label_text = self.subjects[label]
				(x, y, w, h) = rect
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				self.nametext.delete(0,END)
				self.nametext.insert(0, label_text)
				x,y = rect[0],rect[1]-5
				cv2.putText(frame, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
			else:
				self.nametext.delete(0,END)
			return (ret, frame)
		else:
			return (ret, None)

	def update(self):
		if self.acces == 1:
			ret, frame = self.vid.get_frame()
		else:
			ret, frame = self.frame()

		

		if ret:
			frame = cv2.resize(frame,(380,350))
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))

			self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
		self.window.after(self.delay, self.update)
	def new_data(self):
		self.nametext.delete(0,END)
		self.acces = 1
		self.new["text"]="Update"
		self.new["command"] = self.update_data
		self.labeltext["text"] = "Enter your name. Press on Capture. \n\nAfter few Clicks, click on update"
		self.cancel_button = tkinter.Button(self.window, text="Cancel",command = self.cancel)
		self.cancel_button.grid(row=4, column=3 )
		path = "."
		path+="/train"
		files = os.listdir(path)
		num = 1
		for x in files:
			if num<int(x[1:]):
				num = int(x[1:])
		self.folder = path+"/s"+str(num+1)
		os.mkdir(self.folder)
		self.btn_snapshot['command'] = self.data_capture
		
		
	def data_capture(self):
		ret, frame = self.vid.get_frame()
		face, rect = self.detect_face(frame)
		if rect.any()!=0:
			cv2.imwrite(self.folder+"/" + str(self.count) + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
			self.labeltext["text"] = "Enter your name. 'N' Click on update\n Captured : "+str(self.count)
			self.count+=1
		else:
			self.labeltext["text"] = "Face not detected\nPlease try again"
	def update_data(self):
		new_name = self.nametext.get()
		while new_name == "":
			new_name = pyautogui.prompt('Please enter your Name!')
		if self.count==1:
			pyautogui.alert('Please Capture atleast one photo')
		else:
			self.subjects.append(new_name)
			a = open("tkcv.py","r+")
			a.seek(7456)
			sub = "subjects = "+str(self.subjects)
			a.write(sub+"\nApp(tkinter.Tk(), 'Tkinter and OpenCV',subjects)")
			self.labeltext["text"] = "Successfully created new data\n Restart application to take action on New Data"
			self.labeltime = time.time()
			self.labeltime+=5
			self.acces = 0
			self.new["text"] = "New Data"
			self.new["command"] = self.new_data
			self.cancel_button.destroy()
			self.count=1
			self.btn_snapshot['command'] = self.snapshot
	def cancel(self):
		shutil.rmtree(self.folder)
		self.labeltext["text"] = "Cancelled"
		self.labeltime = time.time()
		self.labeltime+=2
		self.acces = 0
		self.new["text"] = "New Data"
		self.new["command"] = self.new_data
		self.cancel_button.destroy()
		self.count=1
		self.btn_snapshot['command'] = self.snapshot
class MyVideoCapture:
	def __init__(self):
		video_source = 0
		self.vid = cv2.VideoCapture(video_source)
		if not self.vid.isOpened():
			raise ValueError("Unable to open video source", video_source)
			# Get video source width and height
		self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

	def get_frame(self):
		if self.vid.isOpened():
			ret, frame = self.vid.read()
			if ret:
				#cv2.resize(frame,(1,32))
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

			else:
				return (ret, None)
		else:
			return (ret, None)
	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()
subjects = ['', 'Unknown', 'Sreekanth']
App(tkinter.Tk(), 'Tkinter and OpenCV',subjects)