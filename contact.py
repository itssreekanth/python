import pandas as pd
import numpy as np
df = pd.DataFrame()
import names,contacts
nam = names.name()
nam1 = []
nam = np.random.choice(nam,30)
for x in nam:
	x+=" P2"
	nam1.append(x)
contac = contacts.contact()
last = []
for x in nam1:
	last.append("")
#df.drop('Unnamed: 0')
df['last_name'] = last
df['first_name'] = nam1
df['org'] = last
df['title'] = last
df['phone'] = contac[236+136+60+30:236+136+60+30+len(nam1)]
df['email'] = last
df['website'] = last
df['street'] = last
df['city'] = last
df['p_code'] = last
df['country'] = last
#df.drop('Unnamed: 0',inplace = True,axis = 1)
df.to_csv('contacts4.csv')
#df.drop('Unnamed: 0')
print(df.columns)
