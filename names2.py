import requests 
from bs4 import BeautifulSoup
import random as rd
def name():
	url=open("ts.html","r")
	url=url.read()
	soup=BeautifulSoup(url,'html.parser')
	names = []
	all_list = []
	count = 0
	import allnames
	name = allnames.allnames()
	for text in soup.find_all('td'):
		if count==0:
			name.append(text.get_text())
			count=1
		else:
			count=0
	return name
print(name())

#name.append(name())
f = open('allnames.py','w')
f.write("def allnames():\n\tname = ")
f.write(str(name()))
f.write('\n\t')
f.write('return name')