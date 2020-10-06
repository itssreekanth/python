'''import contactslist as cont
import contactslist1 as cont1
import contactslist2 as cont2
num = cont.number()
num1 = cont1.number()
num2 = cont2.number()
set_num = set(num)
set_num1 = set(num1)
set_num2 = set(num2)
f_set = (set_num.union(set_num1)).union(set_num2)
#print(len(list(f_set)))
#print(len(num))
#print(len(num1))
#print(len(num2))
#print(list(f_set))'''
import allcontact
contact = allcontact.allcontacts()
for y,x in enumerate(contact):
	if x[8]==' ':
		x = x[:8]+x[9]+' '+x[9:12]+x[13:]
		contact[y] = x
f = open('allcontact.py','w')
f.write('def allcontacts():\n\tcontacts = ')
f.write(str(contact))
f.write('\n\treturn contacts')

