import requests 
from bs4 import BeautifulSoup 
import webbrowser as wb
from gtts import gTTS as speech
from playsound import playsound as ps
#url=open("Webpage","r") 
#url=url.read()
url=requests.get("https://vitux.com/how-to-change-sudo-password-in-ubuntu/")
soup=BeautifulSoup(url.text,'html.parser')
print("Successfully opened webpage...")
title_of_page=soup.title.string
title_print=title_of_page[0].upper()+title_of_page[1:]#To print first letter uppercase
print("Title : ",title_print)
main_text=[]
link_list=[]
about_list=[]
about1_list=[]
fi=open("text.txt","w")
fil=open("test.txt","w")
te=soup.get_text()
def in_depth():
	count=0
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class!=None:
			if len(link_class)>=1:
				link_class1=link_class[0]
			if link_class1=="inner-wrap":
				for text_1 in text.find_all("p"):			
					text1=text_1.get_text()
					print(text1,"\n")
					convert=speech(text=text1, lang="en")
					convert.save("speech_file.mp3")
					ps("speech_file.mp3")

in_depth()
#print(te)
'''language="en"
convert=speech(text=te, lang=language)
convert.save('test.mp3')
#print(reply)
ps('test.mp3')'''































'''def in_depth():
	count=0
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class!=None:
			if len(link_class)>=1:
				link_class1=link_class[0]
				#print(link_class1)
				if link_class1=="kCrYT":
					for link in text.find_all("a"):
						link1=link.get("href")
						for i in link1:
							if i=="&":
								a=link1.index(i)
								break
						link_list.append(link1[7:a])
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
								if tex_a=="s3v9rd":
									for text_b in text_a.find_all("div"):
										tex_b=text_b.get("class")
										if tex_b!=None:
											if len(tex_b)>=2:
												tex_b=tex_b[1]
											if tex_b=="s3v9rd":
												tex1=text_b.get_text()
										#		for text_c in text_b.find_all("span"):
										#			tex_c=text_c.get("class")
													#print(tex_c)
										#			if tex_c!=None:
										#				if len(tex_c)>=1:
										#					tex_c=tex_c[0]
										#				if tex_c=="BNeawe":															
										#					main_text.append(" ")
												about_list.append(tex1)
												print(tex1)
									#	if count%2!=0:
									#			fi.write("\n")
									#			fi.write(tex1)
									#			fil.write("\n")
									#			fil.write(tex2)
					elif count==0:
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

print("\nThese are results for your search : \n")
in_depth()		'''	
'''
for i in about1_list:
	print(i)
print("\n",main_text[0],"\n")
for i in range(0,len(about_list)):
	print(main_text[i+1])
	print("\n(",about_list[i],(")\n"))'''
#print(link_list)
#wb.open_new_tab(link_list[6])
#print(link_list)
			#for text1 in text.find_all("a"):
			#	link=text1.get("href")
			#	link=text1.get_text()
			#	print(link)
			#	link_list.append(link)
#print(about_list)