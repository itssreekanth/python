import requests 
from bs4 import BeautifulSoup 
import webbrowser as wb
from gtts import gTTS as speech
from playsound import playsound as ps
#url=open("Webpage","r") 
#url=url.read()
url=requests.get("https://www.wikihow.com/Eat-Chicken")
soup=BeautifulSoup(url.text,'html.parser')
print("Successfully opened webpage...")
title_of_page=soup.title.string
title_print=title_of_page[0].upper()+title_of_page[1:]#To print first letter uppercase
print("Title : ",title_print)
main_text=[]
link_list=[]
about_list=[]
about1_list=[]
span_list=[]
check_link=set()
set_text=set()
fi=open("text.txt","w")
fil=open("test.txt","w")
te=soup.get_text()
count=0

for text in soup.find_all("div"):
	link_class=text.get("class")
	if link_class!=None:
		if len(link_class)>=1:
			link_class1=link_class[0]
		if link_class1=="section":
			for text_f in text.find_all('div'):
				text_4=text_f.get('id')
				if text_4=="summary_wrapper":
					tex_f=text_f.get_text()
					print(tex_f[:16],"\n",tex_f[17:-35])
print("Select one of the following: ")
print("")
def in_depth():
	count=0
	for text in soup.find_all("div"):
		link_class=text.get("class")
		if link_class!=None:
			if len(link_class)>=1:
				link_class1=link_class[0]
				if link_class1=="mw-parser-output":
					for text_a in text.find_all("div"):
						tex_a=text_a.get("id")
						if tex_a!=None:
							if len(tex_a)>=1:
								tex_a=tex_a[0]
							if tex_a=="":
								for text_b in text_a.find_all("a"):
									link_1=text_b.get("href")
									tex1=text_b.get_text()
									tex2=text_b.prettify()
									about1_list.append(tex1[6:])
									print(tex1[6:])
					inp=input("Select one from above are press 'Enter' to show full article:")
					if inp=='':
						for text_a in text.find_all("div"):
							tex_a=text_a.get("class")
							if tex_a!=None:
								if len(tex_a)>=1:
									tex_b=tex_a[0]
								if len(tex_a)>=2:
									tex_e=tex_a[1]
							if tex_b=="mf-section-0":
								tex=text_a.get_text()
								print(tex)
							if tex_b=="section":
								for span_a in text_a.find_all("h3"):
									spa_a=span_a.get_text()
									print(spa_a)
									text_1=''
									for text_b in text_a.find_all("div"):
										tex2=text_b.get("class")
										if tex2!=None:
											if len(tex2)>=1:
												tex2=tex2[0]
												if tex2=="step":
													text_1+=text_b.get_text()
									print(text_1)
							if tex_e=="warnings":
								for text_d in text_a.find_all("h2"):
									tex_d=text_d.get_text()
									print(tex_d)
								for text_c in text_a.find_all("div"):
									tex_c=text_c.get('class')
									if tex_c==None:
										tex3=text_c.get_text()
										print(tex3)
										main_text.append(tex3)
					else:
						text_1=''
						for text_a in text.find_all("div"):
							tex_a=text_a.get("class")
							#print(tex_a)
							if tex_a!=None:
								if len(tex_a)>=1:
									tex_b=tex_a[0]
								if len(tex_a)>=2:
									tex_e=tex_a[1]
							if tex_b=="section_text":
								for text_b in text_a.find_all("div"):
									tex2=text_b.get("class")
									if tex2!=None:
										if len(tex2)>=1:
											tex2=tex2[0]
											if tex2=="step":
												text_1+=text_b.get_text()
								if text_1!="":
									main_text.append(text_1)
								text_1=''
							if tex_e=="warnings":
								for text_d in text_a.find_all("h2"):
									tex_d=text_d.get_text()
								for text_c in text_a.find_all("div"):
									tex_c=text_c.get('class')
									if tex_c==None:
										tex3=text_c.get_text()
										tex_d+=tex3
										main_text.append(tex_d)
						set_text=set()
						inp=inp.lower()
						inp=inp.split(" ")
						for i in inp:
							check_link.add(i)
							high=0
						for i in range(0,(len(about1_list))):
							test=about1_list[i]
							test=test[:-11]
							main_text2=test.split(" ")
							for j in main_text2:
								j=j.lower()
								set_text.add(j)
							len_intersection=len(set_text.intersection(check_link))
							if len_intersection>=high:
								high=len_intersection
								link_to_print=main_text[i]
							set_text=set()
							if i>=len(about1_list)-1:
								print(link_to_print)
								link_to_print=[]
in_depth()

					#convert=speech(text=text1, lang="en")
					#convert.save("speech_file.mp3")
					#ps("speech_file.mp3")


				#	engine.say(text1)
				#	engine.runAndWait()
				#	engine.stop()

#print(te)
'''language="en"
convert=speech(text=te, lang=language)
convert.save('test.mp3')
#print(reply)
ps('test.mp3')'''


