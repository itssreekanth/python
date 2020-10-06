#print('\a')
# sudo apt install sox
import os
'''for x in range(1000):
	os.system('play -nq -t alsa synth {} sine {}'.format(0.5,x))'''
os.system('play -nq -t alsa synth {} sine {}'.format(1,5000))