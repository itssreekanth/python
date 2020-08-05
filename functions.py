import random as rd
from gtts import gTTS as speech
from playsound import playsound as ps
from urllib.request import urlopen
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 155)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id)
tab_space=0
def hi():
	reply=rd.choice(["Hello sir","Hi sir","Hey sir"])
	language='en'
	try:
		urlopen("https://google.co.in")
		output='True'
		if output=='True':
			convert=speech(text=reply, lang=language)
			convert.save("speech_file.mp3")
			print(reply)
			ps("speech_file.mp3")
	except:
		a="Please get online for better speech..."
		print(a)
		engine.say(a)
		engine.runAndWait()
		print(reply)
		engine.say(reply)
		engine.runAndWait()
		engine.stop()
def goodmorning():
	reply=rd.choice(["A very Good morning", "How can I help you","What can I do for you sir"])
	language='en'
	try:
		urlopen("https://google.co.in")
		output='True'
		if output=='True':
			convert=speech(text=reply, lang=language)
			convert.save('Good Morning.mp3')
			print(reply)
			ps('Good Morning.mp3')
	except:
		a="Please get online for better speech..."
		print(a)
		engine.say(a)
		engine.runAndWait()
		print(reply)
		engine.say(reply)
		engine.runAndWait()
		engine.stop()
def myname():
	reply=rd.choice(["actually I don't know myself","Still i am in constructing stage. I will get it by soon","feeling sad to say that I don't have a name to tell","I don't have a name. Suggest me a better one"])
	language='en'
	try:
		urlopen("https://google.co.in")
		output='True'
		if output=='True':
			convert=speech(text=reply, lang=language)
			convert.save('myname.mp3')
			print(reply)
			ps('myname.mp3')
	except:
		a="Please get online for better speech..."
		print(a)
		engine.say(a)
		engine.runAndWait()
		print(reply)
		engine.say(reply)
		engine.runAndWait()
		engine.stop()
def howami():
	reply=rd.choice(["Fine","Nice","Good","Not bad","cool"])
	language='en'
	try:
		urlopen("https://google.co.in")
		output='True'
		if output=='True':
			convert=speech(text=reply, lang=language)
			convert.save(reply+'.mp3')	
			print(reply)
			ps('howami.mp3')
	except:
		a="Please get online for better speech..."
		print(a)
		engine.say(a)
		engine.runAndWait()
		print(reply)
		engine.say(reply)
		engine.runAndWait()
		engine.stop()
def howdoudoing():
	reply=rd.choice(["Not bad","Good","Nice","As well as I can","Fine"])
	language='en'
	try:
		urlopen('https://google.co.in')
		output='True'
		if output=='True':
			convert=speech(text=reply, lang=language)
			convert.save('howdoudoing.mp3')	
			print(reply)
			ps('howdoudoing.mp3')
	except:
		a="Please get online for better speech..."
		print(a)
		engine.say(a)
		engine.runAndWait()
		print(reply)
		engine.say(reply)
		engine.runAndWait()
		engine.stop()
def teja():
	reply=rd.choice(["hi teja","pora vada"])
	language='en'
	try:
		urlopen('https://google.co.in')
		output='True'
		if output=='True':
			convert=speech(text=reply, lang=language)
			convert.save('teja.mp3')
			print(reply)
			ps('teja.mp3')
	except:
		a="Please get online for better speech..."
		print(a)
		engine.say(a)
		engine.runAndWait()
		print(reply)
		engine.say(reply)
		engine.runAndWait()
		engine.stop()
def write_py_program():
	file_name=input("Enter the file name:")
	read_mode=input("Enter the read mode:")
	f=open("test1.py","rb+")
	lines=f.readlines()
	first_line=lines[0]
	line=lines[1]
	length=len(line)
	f.seek(12,0)
	op="f = open('"+file_name+"','"+read_mode+"')"
	input_len=len(op)
	space=length-input_len
	space=" "*(space-2)
	f.write(op.encode())
	f.write(space.encode())
	import test1 as tt
	tt.allfunctions()