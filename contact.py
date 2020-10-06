import pandas as pd
import numpy as np
df1 = pd.read_csv('allcontacts1.csv')
df = pd.DataFrame()
import allnames,allcontact
nam = allnames.allnames()
nam1 = []
nam = np.random.choice(nam,20,replace=False)
for x in nam:
	x+=" ecell"
	nam1.append(x)
phone = allcontact.allcontacts()
last = []
for x in nam1:
	last.append("")
#df.drop('Unnamed: 0')

#nam1 = df1['first_name']
#last = []
#for x in nam1:
	#last.append("")
#phone = df1['phone']
for y,x in enumerate(phone):
	if x[8]==' ':
		x = x[:8]+x[9]+' '+x[10:12]+x[13:]
		phone[y] = x

df['last_name'] = last
df['first_name'] = nam1
df['org'] = last
df['title'] = last
df['phone'] = phone[810:len(nam1)+810]
df['email'] = last
df['website'] = last
df['street'] = last
df['city'] = last
df['p_code'] = last
df['country'] = last
#df.drop('Unnamed: 0',inplace = True,axis = 1)
df2 = df1.append(df,ignore_index=True)
df2.to_csv('allcontacts1.csv',index = False)
#df.drop('Unnamed: 0')
#print(df)
print(df2)
print(len(nam1))
nam2 = set(nam1)
nam2 = list(nam2)
print(len(nam2))