import subprocess
record=subprocess.getoutput("termux-speech-to-text")
print (record)