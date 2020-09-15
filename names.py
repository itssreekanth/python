import requests 
from bs4 import BeautifulSoup
import random as rd
def name():
	url=open("ta.html","r")
	url=url.read()
	soup=BeautifulSoup(url,'html.parser')
	names = []
	all_list = []
	for text in soup.find_all('h3'):
		text1 = text.get_text()
		if ';' in text1:
			text1 = text1[::-1]
			index = text1.index(';')
			text1 = text1[::-1]
			text1 = text1[-index:]
			names.append(text1)
		else:
			names.append(text1)
	names = set(names)
	names = list(names)
	#print(rd.choice(names))
	return names
#print(len(name()))