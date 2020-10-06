import requests 
from bs4 import BeautifulSoup
def contact():
	url=open("WhatsApp3.html","r")
	url=url.read()
	#print(url)
	soup=BeautifulSoup(url,'html.parser')
	#print(soup)
	all_list = []
	for text in soup.find_all('span'):
		text1 = text.get_text()
		if text1!=None:
			if text1!='':
				all_list.append(text1)
	dup_set = set(all_list)
	all_list = list(dup_set)
	numbers = []
	for x in all_list:
		if '+91' in x:
			if len(x)>16:
				#print(x)
				count = 0
				num = ''
				for y in x:
					count+=1
					if y=='+':
						if x[count]=='9' and x[count+1]=='1':
							if x[count+11]==' ':
								extra = x[count-1:count+15]
							else:
								extra = x[count-1:count+14]
							numbers.append(extra)

						


			if len(x)==15:
				numbers.append(x)
		count=0
	numbers = set(numbers)
	numbers = list(numbers)
	return numbers
a = contact()
f = open('contacts2.txt','w+')
f.write('num = ')
f.write(str(a))