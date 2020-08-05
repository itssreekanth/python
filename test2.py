import requests 
from bs4 import BeautifulSoup 
import webbrowser as wb
url=requests.get("https://www.wikihow.com/Eat-Chicken")

soup=BeautifulSoup(url.text,'html.parser')
f=open("wikihow","w+")
t=soup.prettify()
f.write(t)
print("Successfully opened webpage...")
title_of_page=soup.title.string
title_print=title_of_page[0].upper()+title_of_page[1:]#To print first letter uppercase
print("Title : ",title_print)
head_text=[]
about_head=[]
link_list=[]
#while True:
	#do=input("What should I Check? : ")
	#if (("headings" in do) or ("header" in do))==True:
def headers():
	print("These are in Webpage:")
	for text in soup.find_all("h3"):
		clas=text.get_text()
		print(clas)
		head_text.append(clas)
def headers_about():
	for text in soup.find_all('span'):
		clas=text.get('class')
		if clas!=None:
			if len(clas)>=1:
				clas=clas[0]
			if clas=="st":
				about1=text.get_text()
				print(about1,"\n")
				about_head.append(about1)
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class=="rc":
			for text1 in text.find_all("a"):
				link=text1.get("href")
				link=text1.get_text()
				print(link)
				link_list.append(link)
def links():
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class!=None:
			if len(link_class)>=1:
				clas=link_class[0]
			if clas=="ZINbbc":
				link
				for text1 in text.find_all("a"):
					#link=text1.get("href")
					link=text1.get_text()
					#print(link,"yes")
					link_list.append(link)
				for text1 in text.find_all("h3"):
					clas=text1.get_text()
					#print(clas)
					head_text.append(clas)
				for text1 in text.find_all('span'):
					clas=text1.get('class')
					if clas!=None:
						if len(clas)>=1:
							clas=clas[0]
					if clas=="st":
						about1=text.get_text()
						#print(about1,"\n")
						about_head.append(about1)
links()
headers()
headers_about()
#print(links)
for i in range(0,(len(about_head))):
	print(head_text[i],"\n")
	print("(",about_head[i],")","\n")
