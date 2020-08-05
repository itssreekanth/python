while True:
	print()
	a = input("Enter the number : ")
	print("")
	if a=="q":
		break
	else:
		a = int(a)
		for x in range(1,10):
			print("\t",a," x ",x," = ",a*x)
		print("\t",a," x ",10,"= ",a*10)