import requests 
from bs4 import BeautifulSoup
url=open("telugua.html","r")
url=url.read()
soup=BeautifulSoup(url,'html.parser')
names = []
all_list = []
for text in soup.find_all('a'):
	text1 = text.get_text()
	print(text1)
	#names.append(text1)
#print(len(names))