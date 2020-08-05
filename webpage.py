import requests 
from bs4 import BeautifulSoup 
import webbrowser as wb
f=open("webpage2","a+")
inpu=input("Enter a html file:")
inpu=inpu+".html"
url=open(inpu,"r")
url=url.read()
soup=BeautifulSoup(url,'html.parser')
menu=[]
link=[]
about=[]
components=[]
link_main=[]
set_links=[]
check_link=set()
list_text=[]
set_text=set()
high=0
result_set=set()
print("Successfully opened webpage.")
print(soup.title.string)
for text in soup.find_all('div'):
	clas=text.get('class')
	if clas!=None:
		if len(clas)>=1:
			clas=clas[0]
			f.write(clas)
			f.write("\n")
	if clas=="media-heading":
		for text1 in text.find_all('a'):
			about1=text1.get_text()
			about.append(about1)
#print(about)
for text in soup.find_all('h2'):
	for li in text.find_all('a'):
		link_main1=li.get("href")
		link_main.append(link_main1)
num=0
while True:
	do=input("What should I Check? : ")
	if (("headings" in do) or ("header" in do))==True:
		print("These are in Webpage:")
		for text in soup.find_all('h2'):
			clas=text.get_text()
			clas1=''.join(clas)
			print(clas1)
			components.append(clas)
		for text in soup.find_all('h2'):
			for li in soup.find_all('a'):
				link_main1=li.get("href")
				link_main.append(link_main1)
		while True:
			do2=input("Do you want to see content below the above headings (y/n):")
			if ("y" in do2)==True:
				while True:
					do3=input("Which one do you want to know:")
					if do3!='q':
						for text2 in soup.find_all('div'):
							text3=text2.get("media-body top-news-text")
							if text3!=None:
								if str(text3)==do3:
									for text4 in text2.find_all('a'):
										final=text4.get_text()
										list_text.append(final)
										print(final)
										links=text4.get("href")
										set_links.append(links)
									if set_links!=set():
										inp=input("Looks like some are link's type keywords to open it : ")
										inp=inp.split(" ")
										for i in inp:
											check_link.add(i)
										for i in range(0,len(list_text)):
											test=list_text[i]
											list_text1=test.split(" ")
											for j in list_text1:
												set_text.add(j)
												len_intersection=len(set_text.intersection(check_link))
												if len_intersection>=high:
													high=len_intersection												
													link_to_print=set_links[i]
											set_text=set()
											if i>=len(list_text)-1:
												print(link_to_print)
					else:
						break
			elif("link" in do2)==True or ("open" in do2):
				while True:
					do3=input("Which one do I open:")
					ch=do3.split(" ")
					for i in ch:
						for j in components:
							if (i in j) and i!="Install":
								wb.open(link_main[num])
							num+=1
						num=0
					break
			elif("q" in do2)==True:
				break

	elif("q" in do):
		break		
'''for text in soup.find_all('div'):
	clas=text.get('class')
	if clas!=None:
		clas=clas[0]	
		#print(type(clas))
	if clas=="header-menu":
		print("Following are in Header-Menu:")
		for text1 in text.find_all('a'):
			menu1=text1.get_text()
			link1=text1.get("href")
			link.append(link1)
			a=''.join(menu1)
			print(a)
			menu.append(a)
		while True:
			select=input("Select one from above:")
			if select==menu[0]:
				wb.open_new_tab(link[0])
			elif select==menu[1]:
				wb.open_new_tab(link[1])
			elif select==menu[2]:
				wb.open_new_tab(link[2])
			elif select==menu[3]:
				wb.open_new_tab(link[3])
			elif select==menu[4]:
				wb.open_new_tab(link[4])
			elif select==menu[5]:
				wb.open_new_tab(link[5])
			elif select==menu[6]:
				wb.open_new_tab(link[6])
			elif select==menu[7]:
				wb.open_new_tab(link[7])
			elif select=="q" or select=="quit":
				break
	if clas=="resumo":
		print("Following are in Webpage:")
		for text1 in text.find_all('span'):
			about1=text1.get_text()
			about.append(about1)
while True:
			select=input("Select one from above:")
			if select==menu[0]:
				wb.open_new_tab(link[0])
			elif select==menu[1]:
				wb.open_new_tab(link[1])
			elif select==menu[2]:
				wb.open_new_tab(link[2])
			elif select==menu[3]:
				wb.open_new_tab(link[3])
			elif select==menu[4]:
				wb.open_new_tab(link[4])
			elif select==menu[5]:
				wb.open_new_tab(link[5])
			elif select==menu[6]:
				wb.open_new_tab(link[6])
			elif select==menu[7]:
				wb.open_new_tab(link[7])
			elif select=="q" or select=="quit":
				break'''
#print(about)
#text=soup.get_text()
#f.write(text)