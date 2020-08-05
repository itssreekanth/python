import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
rate=engine.setProperty('rate', 150)     # setting up new voice rate
print (rate)

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#volume=engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
print (volume)
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice

#print(len(voices))
#for i in range(0,len(voices)):
#	print(i)
a=input("Say Something:")
#for i in range(0,len(voices)):
#	print(i)
engine.setProperty('voice', voices[14].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
	#a=input("Say Something:")
engine.say(a)
engine.runAndWait()
engine.stop()




















'''


from gtts import gTTS 
from playsound import playsound
while True:
    mytext = input("Say Something:")
#mytext1="How are you"
    language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high spee
    myobj = gTTS(text=mytext, lang=language)
#myobj1 = gTTS(text=mytext1, lang=language, slow=False)
# Saving the converted audio in a mp3 file named 
# welcome  
    myobj.save("offlineresult.mp3") 
    print("successfully retrieved voice...")
#myobj1.save("welcome1.mp3")
# Playing the converted file 
    playsound("offlineresult.mp3")
        
    if mytext=='q':
        break
#playsound("welcome1.mp3")'''