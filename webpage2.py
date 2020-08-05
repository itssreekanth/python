#the code should be its own analyzing
import requests 
from bs4 import BeautifulSoup 
import webbrowser as wb
search=input("Do a google search now :")
search="http://www.google.com/search?btnG=1&q="+search
url=requests.get(search)
soup=BeautifulSoup(url.text,'html.parser')
print("Successfully opened webpage...")
title_of_page=soup.title.string
title_print=title_of_page[0].upper()+title_of_page[1:]#To print first letter uppercase
print("Title : ",title_print,"\n")#prints the title of the webpage
main_text=[]
link_list=[]
link_list1=[]
about_list=[]
about1_list=[]
def header():
	for text_a in soup.find_all("div"):
		tex_a=text_a.get("class")
		if tex_a!=None:
			if len(tex_a)>=2:
				tex_a=tex_a[1]
			if tex_a=="vvjwJb":
				text1=text_a.get_text()
				main_text.append(text1)
def links():
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class!=None:
			if len(link_class)>=1:
				link_class1=link_class[0]
				if link_class1=="kCrYT":
					for link in text.find_all("a"):
						link1=link.get("href")
						for i in link1:
							if i=="&":
								a=link1.index(i)
								break
					for text_a in text.find_all("div"):
							tex_a=text_a.get("class")
							if tex_a!=None:
								if len(tex_a)>=2:
									tex_a=tex_a[1]
								if tex_a=="vvjwJb":
									#text1=text_a.get_text()
									#print(text1)
									#main_text.append(text1)
									#print(text1)
									link_list.append(link1[7:a])
def in_depth():
	count=0
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class!=None:
			if len(link_class)>=1:
				link_class1=link_class[0]
				if link_class1=="kCrYT":
					for link in text.find_all("a"):
						link1=link.get("href")
						for i in link1:
							if i=="&":
								a=link1.index(i)
								break
						#link_list.append(link1[7:a])
						count=1
					if count==1:
						for text_a in text.find_all("div"):
							tex_a=text_a.get("class")
							if tex_a!=None:
								if len(tex_a)>=2:
									tex_a=tex_a[1]
								if tex_a=="vvjwJb":
									text1=text_a.get_text()
									#print(text1)
									main_text.append(text1)
									print(text1)
									link_list.append(link1[7:a])
								if tex_a=="s3v9rd":
									for text_b in text_a.find_all("div"):
										tex_b=text_b.get("class")
										if tex_b!=None:
											if len(tex_b)>=2:
												tex_b=tex_b[1]
											if tex_b=="s3v9rd":
												tex1=text_b.get_text()
												about_list.append(tex1)
												print("(",tex1,")\n")
					elif count==0:
						link_list.append(" ")
						for text_a in text.find_all("div"):
							tex_a=text_a.get("class")
							if tex_a!=None:
								if len(tex_a)>=2:
									tex_a=tex_a[1]
								if tex_a=="s3v9rd":
									for text_b in text_a.find_all("div"):
										tex_b=text_b.get("class")
										if tex_b!=None:
											if len(tex_b)>=2:
												tex_b=tex_b[1]
											if tex_b=="s3v9rd":
												tex1=text_b.get_text()
												tex2=text_b.prettify()
												about1_list.append(tex1)
												print(tex1)
												link_list.append(" ")
header()
if len(about1_list)!=0:
	print(about1_list,"\n")
print("\n")
for i in main_text:
	print(i)
while True:
	check_link=set()
	set_text=set()
	inpu=input("\n Enter 'About' to get description... \n Are type keywords to open link : ")
	inpu=inpu.lower()
	if inpu=="about":
		in_depth()
	elif inpu=="q" or inpu=="quit":
		break
	else:
		inp=inpu.split(" ")
		for i in inp:
			check_link.add(i)
		high=0
		links()
		for i in range(0,len(main_text)):
			test=main_text[i]
			main_text2=test.split(" ")
			for j in main_text2:
				j=j.lower()
				set_text.add(j)
			len_intersection=len(set_text.intersection(check_link))
			if len_intersection>=high:
				high=len_intersection												
				link_to_print=link_list[i]
			set_text=set()
			if i>=len(main_text)-1:
				wb.open_new_tab(link_to_print)
				print(link_to_print)
				link_to_print=[]
			
