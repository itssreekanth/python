import os
from subprocess import Popen, PIPE, STDOUT
from urllib.request import urlopen
from tqdm import tqdm
from time import sleep
def is_internet_available():#To check is system connected to internet
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except:
        return False
if True:
	print("Welcome...")
	os.system("sudo dpkg --add-architecture i386")
	urllib.request.urlretrieve('https://dl.winehq.org/wine-builds/winehq.key','winehq.key')
	key = os.popen("sudo apt-key add winehq.key").readlines()
	print(key)
	key = ["OK"]
	if "OK" in key[0]:
		print("Adding repository please wait...")
		os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main' && sudo apt update")
		print("Please press 'n' if packages to be removed are more in the below command.")
		for i in range(5):
		    print("Wait time : {}s/5s".format(i),end = "\r")
			time.sleep(1)
		os.system("sudo apt install --install-recommends winehq-stable")
		installed = os.popen('wine --version')
		installed = installed.readlines()
		if len(installed) == 1 and "wine" in installed[0]:
			print(installed)
			print('complete')
		else:
			for i in installed:
				if "not found" in i:
					install = os.popen("sudo apt-get install --install-recommends winehq-stable")
					install = install.readlines()
					for j in install:
						if "unmet" in j:
							os.system("wget https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/amd64/libfaudio0_19.07-0~bionic_amd64.deb")
							os.system("wget https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/i386/libfaudio0_19.07-0~bionic_i386.deb")
							os.system("sudo dpkg -i libfaudio0_19.07-0~bionic_amd64.deb libfaudio0_19.07-0~bionic_i386.deb")
							os.system("sudo apt --fix-broken install")
							os.system("sudo apt update")
							print("Please press 'n' if packages to be removed are more in the below command.")
							for i in range(3):
								print("Wait time : {}s/3s".format(i),end = "\r")
								time.sleep(1)
							os.system("sudo apt install --install-recommends winehq-stable")
						elif "dpkg" in j:
							print("Please restart the system and re-try.")
						else:
							for k in install:
								print(k)
							print("Above is the error")
		installed = os.popen('wine --version')
		installed = installed.readlines()
		if len(installed) == 1 and "wine" in installed[0]:
			print(installed)
			print('complete')
		else:
			print("Please raise the error you got.")
	else:
		print("Can't add repo key")