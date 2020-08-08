import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import numpy as np

class App:
    def __init__(self, window, window_title,subjects,video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.subjects = subjects
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.subjects)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15

        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
	def __init__(self,subjects):
		self.subjects = subjects
		video_source = 0
		self.vid = cv2.VideoCapture(video_source)
		if not self.vid.isOpened():
			raise ValueError("Unable to open video source", video_source)
			# Get video source width and height
		self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
		self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
	def detect_face(self,img):
		#convert the test image to gray image as opencv face detector expects gray images
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#load OpenCV face detector, I am using LBP which is fast
		#there is also a more accurate but slow Haar classifier
		face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
		#let's detect multiscale (some images may be closer to camera than others) images
		#result is a list of faces
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
		#if no faces are detected then return original img
		if (len(faces) == 0):
			return None, np.zeros(4)
			#under the assumption that there will be only one face
			#extract the face area
		(x, y, w, h) = faces[0]
		#return only the face part of the image
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
				cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
				cv2.waitKey(100)
				face, rect = detect_face(image)
				if face is not None:
					faces.append(face)
					labels.append(label)
		cv2.destroyAllWindows()
		cv2.waitKey(1)
		cv2.destroyAllWindows()
		return faces, labels
	def training(self):
		print("Preparing data...")
		faces, labels = self.prepare_training_data("training-data")
		print("Data prepared")
		print("Total faces: ", len(faces))
		print("Total labels: ", len(labels))
		self.face_recognizer.train(faces, np.array(labels))
	def get_frame(self):
		if self.vid.isOpened():
			ret, frame = self.vid.read()
			if ret:
				img = frame.copy()
				face, rect = self.detect_face(img)
				#label,confidence = self.face_recognizer.predict(face)
				#label_text = self.subjects[label]
				if rect.any() != 0:
					(x, y, w, h) = rect
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
					x,y = rect[0],rect[1]-5
					#cv2.putText(frame, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (ret, None)
	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()
subjects = ["", "Ramiz Raja", "Elvis Presley"]
App(tkinter.Tk(), "Tkinter and OpenCV",subjects)