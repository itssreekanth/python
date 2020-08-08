import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time,os
import numpy as np

class App:
	def __init__(self, window, window_title,subjects,video_source=0):
		self.window = window
		self.window.title(window_title)
		self.video_source = video_source
		self.subjects = subjects
		self.vid = MyVideoCapture()
		self.canvas = tkinter.Canvas(window, width = 380, height = 380)
		self.canvas.grid(row=0, column=0,columnspan=1,rowspan = 4 ,padx=5)
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
		self.new = tkinter.Button(window, text="new", bg="orange", fg="black")
		self.new.grid(row=3, column=2 )
		self.btn_snapshot = tkinter.Button(window, text="capture", bg="skyblue", fg="black", command=self.snapshot)
		self.btn_snapshot.grid(row=3, column=4 )
		self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
		self.training()
		self.delay = 15
		self.update()
		self.window.mainloop()
	def snapshot(self):

		ret, frame = self.vid.get_frame()
		if ret:
			cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
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
		ret, frame = self.vid.get_frame()
		if ret:
			img = frame.copy()
			face, rect = self.detect_face(img)
			if rect.any() != 0:
				label,confidence = self.face_recognizer.predict(face)
				label_text = self.subjects[label]
				(x, y, w, h) = rect
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				x,y = rect[0],rect[1]-5
				cv2.putText(frame, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
			return (ret, frame)
		else:
			return (ret, None)

	def update(self):
		ret, frame = self.frame()
		if ret:
			#cv2.resize(frame,(280,480))
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
			self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
		self.window.after(self.delay, self.update)
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

				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (ret, None)
	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()
subjects = ["", "Unknown","Sreekanth", "Elvis Presley"]
App(tkinter.Tk(), "Tkinter and OpenCV",subjects)