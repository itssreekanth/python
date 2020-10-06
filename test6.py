import os,subprocess
#os.system("sudo apt update && sudo apt install python3-pip && sudo apt install python3-tk && python3 -m pip install pyscreenshot && python3 -m pip install pil")
a = os.popen("apt-cache policy sox").readlines()
print('none' in a[1])