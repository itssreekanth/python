tab_space=0
f = open('prime.py','a+')                                                     
def allfunctions():
	def inside_loop():
		global tab_space
		while True:		
			print("Adding to ",tab_space,"loop")
			inp1=input("What next:")
			if ("variable" in inp1)==True:
				variable()
			if ("for" in inp1)==True and ("loop" in inp1)==True:
				for_loop()
				inside_loop()
			if ("write" or "manual" in inp1)==True:
				write_line()
			if ("print" in inp1)==True:
				print1()
			if ("add numbers" or "add variables" in inp1)==True:
				add()
			if ("append" in inp1)==True:
				append()
			if ("from the user" in inp1)==True:
				take()
			if ("if condition" in inp1)==True:
				if_condition()
				inside_loop()
				re=input("Enter 'y' to continue to else_condition:")
				if re=="y":
					else_condition()
					inside_loop()
			if ("exit" in inp1)==True:
				exit_loop()
				break
			if inp1=="q":
				break
			if ("def function" in inp1)==True or ("write a function" in inp1)==True:
				function()
				inside_loop()
			if ("try block" in inp1)==True or ("exceptions" in inp1)==True:
				try_block()
				inside_loop()
				ta=input("press 'y' to enter into except_block:")
				if ta=="y":
					except_block()
				ta1=input("press 'y' to enter into else_condition:")
				if ta1=="y":
					else_condition()
					inside_loop()
				ta2=input("press 'y' to enter into final_block:")
				if ta2=="y":
					final_block()
					inside_loop()
			if ("else condition" in inp1)==True:
				else_condition()
				inside_loop()
			if ("while loop" in inp1)==True:
				while_loop()
				inside_loop()
			if("write the code manually" in inp1)==True or "write manually" in inp1:
				manual()
	def if_condition():
		global tab_space
		global f
		condition=input("What is the condition :")
		ouput1=space*tab_space+"if ("+condition+"):"
		tab_space+=1
		f.write("\n")
		f.write(ouput1)
	def variable():
		global tab_space
		variable=input("Tell me the name of the variable:")
		ouput2=space*tab_space+variable+"="
		a=input("What should I assign to this variable (input from the user ; list ; so on...:")
		if ("from the user" in a)==True:
			a=input("Are you want to add 'int' infront of it (y/n):")
			if a=="y" or a=="Y":
				inp4=input("How to ask you to enter numbers in variable:")
				inp5=input("Successfully added")
				ouput1=ouput2+'int(input("'+inp4+'"))'
				f.write("\n")
				f.write(ouput1)
			else:
				inp4=input("How to ask you to enter numbers in variable:")
				ouput1=ouput2+'input("'+inp4+'")'
				f.write("\n")
				f.write(ouput1)
		if("list" in a)==True:
			output=""
			ab=int(input("How many elements to store:"))
			print("If you want to write int or mixed values to list please try 'write manually' method")
			for i in range(ab):
				b=input("Enter the element :")
				if i<ab-1:
					output=output+"'"+b+"'"+","
				else:
					output=output+"'"+b+"'"
			output="["+output+"]"
			print(output)
			ouput1=ouput2+output
			f.write("\n")
			f.write(ouput1)
		if("write the code manually" in a)==True or "write manually" in a:
			a=input("Write the code:")
			ouput1=ouput2+a
			f.write("\n")
			f.write(ouput1)
	def manual():
		a=input("Write the code:")
		ouput1=space*tab_space+a
		f.write("\n")
		f.write(ouput1)
	def append():
		global tab_space
		global f
		inp6=input("Which should I append:")
		inp5=input("for which variable I have to append it:")
		ouput2=space*tab_space+inp5+".append("+inp6+")"
		f.write("\n")
		f.write(ouput2)
	def add():
		global tab_space
		global f
		inp7=input("For which variable should I assign this sum: ")
		inp8=input("Enter the first variable: ")
		inp9=input("Enter the second variable:")
		ouput2=space*tab_space+inp7+"="+inp8+"+"+inp9
		f.write("\n")
		f.write(ouput2)
	def print1():
		global tab_space
		global f
		inp10=input("what should i print:")
		ouput1=space*tab_space+"print("+inp10+")"
		f.write("\n")
		f.write(ouput1)
	def write_line():
		global tab_space
		global f
		inp11=input("write now : ")
		ouput1=space*tab_space+inp11
		f.write("\n")
		f.write(ouput1)
	def for_loop():
		global tab_space
		global f
		inp1=input("complete the condition: for ")
		ouput1=space*tab_space+"for "+inp1+":"
		tab_space+=1
		f.write("\n")
		f.write(ouput1)
	def exit_loop():
		global tab_space
		tab_space-=1
	def take():
		global tab_space
		global f
	def function():
		global f
		global tab_space
		save=input("How should I save the function:")
		ouput1=("def ")+save+("():")
		print("Write the code inside the function")
		tab_space+=1
		f.write("\n")
		f.write(ouput1)
	def try_block():
		global f
		global tab_space
		print("You are in try_block")
		ouput1=space*tab_space+"try:"
		tab_space+=1
		f.write("\n")
		f.write(ouput1)
	def except_block():
		global f
		global tab_space
		print("You are in except_block")
		ho=int(input("How many except block's do you want:"))
		for i in range(ho):
			ouput1="except "
			error=input("Enter the error name:")
			ouput1=space*tab_space+ouput1+error+" as e :"
			f.write("\n")
			f.write(ouput1)
			tab_space+=1
			wha1=input("Do you want to print the name of the error(y/n):")
			if wha1=="yes" or wha1=="y":
				ouput2=space*tab_space+"print(e)"
				f.write("\n")
				f.write(ouput2)
			wha=input("Is their any stuff that I have to add for except_block(y/n)")
			if wha=="yes" or wha=="y":
				inside_loop()
	def else_condition():
		global f
		global tab_space
		ouput1=space*tab_space+"else:"
		tab_space+=1
		print("You are in else_condition")
		f.write("\n")
		f.write(ouput1)
	def final_block():
		global f
		global tab_space
		ouput1=space*tab_space+"finally:"
		tab_space+=1
		print("You are in final_block")
		f.write("\n")
		f.write(ouput1)
	def while_loop():
		global f
		global tab_space
		con=input("Enter the condition:")
		ouput1=space*tab_space+"while "+con+" :"
		tab_space+=1
		print("You are in final_block")
		f.write("\n")
		f.write(ouput1)
	space="	"
	while True:
		inp=input("What can I do for you:")
		if ("variable" in inp)==True:
			variable()
		if ("for" in inp)==True and ("loop" in inp)==True:
			for_loop()
			inside_loop()
		if ("write" or "manual" in inp)==True:
			write_line()
		if ("print" in inp)==True:
			print1()
		if ("add numbers" or "add variables" in inp)==True:
			add()
		if ("append" in inp)==True:
			append()
		if ("user" in inp)==True:
			take()
		if ("if condition" in inp)==True:
			if_condition()
			inside_loop()
			re=input("Enter 'y' to continue to else_condition:")
			if re=="y":
				else_condition()
				inside_loop()
		if inp=="q" or inp=="quit" or inp=="exit":
			break
		if ("def function" in inp)==True or ("write a function" in inp)==True:
			function()
			inside_loop()
		if ("try block" in inp)==True or ("exceptions" in inp)==True:
			try_block()
			inside_loop()
			ta=input("press 'y' to enter into except_block:")
			if ta=="y":
				except_block()
			ta1=input("press 'y' to enter into else_condition:")
			if ta1=="y":
				else_condition()
				inside_loop()
			ta2=input("press 'y' to enter into final_block:")
			if ta2=="y":
				final_block()
				inside_loop()
		if ("else condition" in inp)==True:
			else_condition()
			inside_loop()
		if ("while loop" in inp)==True:
			while_loop()
			inside_loop()
		if("write the code manually" in inp)==True or "write manually" in inp:
			manual()