#if condition
f=open("test.txt","a+")
ouput=""
tab_space=0
space="	"
a="bg hi"
print(a.find("hi"))
inp=input("say something:")
if inp == "if condition":
	tab_space+=1
	condition=input("What is the condition :")
	ouput1=space*tab_space+"if ("+condition+"):"
	f.write("\n")
	f.write(ouput1)
	while True:
		inp1=input("What next:")
		lis=inp1.split()
		if "variable" in lis:
			print("yes")
			inp2=input("Tell me the name of the variable:")
			ouput2=space*tab_space+inp2+"="
			f.write("\n")
			f.write(ouput2)
			if "take" or "store" or "stores" or "input" in lis:
				inp3=input("Are you want to add 'int' infront of it (y/n) :")
				if inp3=="y" or inp3=="Y":
					inp4=input("How to ask you to enter numbers in variable:")
					ouput2=ouput2+'int(input("'+inp4+'")'
					f.write("\n")
					f.write(ouput2)
				else:
					inp4=input("How to ask you to enter numbers in variable:")
					ouput2=ouput2+'input("'+inp4+'")'
					f.write("\n")
					f.write(ouput2)
		if "append" in lis:
			inp6=input("Which should I append:")
			inp5=input("for which variable I have to append it:")
			ouput2=space*tab_space+inp5+".append("+inp6+")"
			f.write("\n")
			f.write(ouput2)
		if "add" in lis:
			inp7=input("For what variable should I save ")
			inp8=input("what should i add")
			inp9=input("what should i add")
			ouput2=space*tab_space+inp7+"="+inp8+"+"+inp9
			f.write("\n")
			f.write(ouput2)
		if "print" in lis:
			inp10=input("what should i print:")
			ouput2=space*tab_space+"print("+inp10+")"
			f.write("\n")
			f.write(ouput2)
		if inp1=="Write a line":
			inp11=input("write now : ")
			ouput2=space*tab_space+inp11
			f.write("\n")
			f.write(ouput2)
		if inp1=="q":
			break


if inp == "for loop":
	inp1=input("complete the condition: for ")
	ouput1==space*tab_space+"for "+inp1+":"
	f.write("\n")
	f.write(ouput1)

