a = []
inp = input("Enter name : ")
out = []
for letter in inp:
	if letter=="a":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==5) and(column>0 and column<7) or ((row>5 or row==4 or row==3) and (column==1 or column==10)) or (row == 0 and column==6) or (row==1 and (column==4 or column==7)) or (row ==2 and(column==2 or column==9))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="b":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 or row==4 or row==8) and(column>0 and column<6) or ((row!=0 or row!=6 or row!=8) and (column==1 or column==10))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="c":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 or row==8) and(column>2 and column<8) or ((row!=0 and row!=8) and (column==1))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="d":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 or row==8) and(column>0 and column<6) or ((row==1 or row==7) and (column==1 or column==10)) or ((row>1 and row<7) and(column==1 or column==11))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="e":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 or row==4 or row==8) and(column>1 and column<7) or ((row!=0 and row!=4 and row!=8) and (column==1))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="f":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0) and(column>0 and column<7) or(row==4 and(column>0 and column<6)) or ((row!=0 and row !=4) and (column==1 ))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="g":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 or row==8) and(column>1 and column<7) or ((row==1 or row<8 and row>4) and (column==1 or column==10)) or (row==4 and(column==1 or column>4 and column<8)) or ((row==2 or row==3) and column==1)):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="h":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==4) and(column>0 and column<8) or ((row!=4) and (column==1 or column==10))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="i":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 or row==8) and(column>1 and column<7) or ((row!=0 and row!=8) and (column==6))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="j":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0) and( column>1 and column<8) or ((row!=0 and row!=8 and row!=7) and (column==8 )) or ((row==8) and(column<6 and column>2)) or(row==7 and (column==2 or column==7)) ):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")		
			store.append(store1)
		out.append(store)
	elif letter=="k":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((column==1) or ((row==0 or row==8) and column==11) or ((row==1 or row==7) and column==9) or ((row==2 or row==6) and column==7) or ((row==3 or row==5) and column==5) or(row==4 and column==3)):
					store1.append("*")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="l":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (column==1 or (row==8 and (column<8 and column>1))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="m":
		store = []
		count = 11
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((column==1 or column==11) or (row+1==column and (column>0 and column<7)) or (row==1 and column==10) or (row==2 and column==9) or (row==3 and column==8) or (row==4 and column==7) or (row==5 and column==6)):
					store1.append("*")
					#store1.append("")
				else:
					store1.append(" ")
			store.append(store1)

		out.append(store)
	elif letter=="n":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((column==1 or column==11) or (row==column-2 and (column>2 and row!=8))):
					store1.append("*")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="o":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row!=0 and row!=8) and (column==1 or column==10)) or ((row==0 or row==8) and (column<7 and column>2))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="p":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row==1 or row==2 or row==3) and (column==1 or column==10)) or ((row==0 or row==4) and (column==1 or column==2 or column==3 or column==4 or column==5)) or column==1):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="q":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row!=0 and row!=7 and row!=8 and row!=7) and (column==1 or column==11)) or ((row==0 or row==7) and (column>1 and column<7)) or (row==6 and(column==1 or column==10 or column==7)) or (row==8 and column==12)):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="r":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row==1 or row==2 or row==3 or row==8) and (column==1 or column==10)) or ((row==0 or row==4) and (column==1 or column==2 or column==3 or column==4 or column==5)) or ((row >4 and row<8) and (column==1 or column==9))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="s":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row==0 or row==4 or row==8) and (column>2 and column<7)) or ((row==1 or row==7) and (column==1 or column==10)) or ((row>1 and row<4) and column==1) or ((row>4 and row<8) and column==11)):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="t":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row==0 and(column>0 and column<7)) or (row!=0 and column==6)):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="u":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((row!=8 and (column==1 or column==10)) or (row==8 and (column>1 and column<7))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="v":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row!=8 and row!=7 and row!=6) and (column==1 or column==10)) or (row==8 and column==6) or (row==7 and (column==4 or column==7)) or (row==6 and(column==2 or column==9))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="w":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if ((column==0 or column==6) or ((row==column+2) and(row>4)) or ((row==6 and column==2) or (row==7 and column==1))):
					store1.append("*")
					store1.append(" ")
				else:
					store1.append("  ")
			store.append(store1)
		out.append(store)
	elif letter=="x":
		store = []
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row==0 or row==1 or row==7 or row==8) and (column==1 or column==11)) or ((row==2 or row==6) and (column==2 or column==10)) or ((row==3 or row==5) and (column==4 or column==8)) or (row==4 and column==6)):
					store1.append("*")
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="y":
		store = []
		count=12
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row+1==column) and (row<5 and column>0)) or ((row+count==column) and (row<5)) or (column==6 and row>4)):
					store1.append("*")
					count-=1
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)
	elif letter=="z":
		store = []
		count=8
		for row in range(9):
			store1 = []
			for column in range(13):
				if (((row+count==column) and (row>1 and row<7)) or ((row==0 or row==8) and (column>1 and column<7)) or ((row==1 or row==7) and (column==1 or column==10))):
					store1.append("*")
					store1.append(" ")
					if ((row+count==column) and (row>1 and row<7)):
						count-=3
				else:
					store1.append(" ")
			store.append(store1)
		out.append(store)





for i in range(9):
	for j in range(len(out)):
		for k in range(13):
			print(out[j][i][k],end = "")
		print(end = "")
	print()
