
a=int(input("Enter the number"))
flag=0
for i in range(2,a):
	if (a%i==0):
		flag=1
if (flag==0):
	print("Given number is a Prime number")
else:
	print("Given number is a composite number")