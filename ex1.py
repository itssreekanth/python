from gtts import gTTS as speech
from playsound import playsound as ps
import functions as fn
import writefunction as wf
import elsecondition as el
import random as rd
function=(dir(fn))
while True:
	text=input("Say Something:")
	if text=="q" or text=="exit" or text=="quit" or text=="Good bye" or text=="bye":
		reply=rd.choice(["Good bye","Good bye sir","Thank you sir","Nice to talking to you good bye","Good bye have a nice day"])
		print(reply)
		break
	elif text=="hi" or text=="hello" or text=="hey":
		fn.hi()
	elif text=='Good Morning' or text=='goodmorning' or text=='hi goodmorning' or text=='good morning':
		fn.goodmorning()
	elif text=="what is your name" or text=="what's your name" or text=="tell me your name" or text=="your name please" or text=="your name":
		fn.myname()
	elif text=="how are you":
		fn.howami()
	elif text=="How are you doing" or text=="how do you doing" or text=="how do you do":
		fn.howdoudoing()
	elif ("python program" in text)==True:
		fn.write_py_program()
	else:
		el.els()