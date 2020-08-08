import os
path = "."
path+="/train"
files = os.listdir(path)
num = 1
for x in files:
	if num<int(x[1:]):
		num = int(x[1:])
		
os.mkdir(path+"/s"+str(num+1))
print(os.listdir(path))