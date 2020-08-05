import time
inp = input("Enter the date : ")
inp = inp.split("/")
inp.reverse()
inp = [int(i) for i in inp]
check_time = tuple(inp)+(0,0,0,0,0,0)
a = time.localtime(time.mktime(check_time))
b = time.localtime()
mont = time.localtime(time.mktime((2020,a.tm_mon,a.tm_mday,0,0,0,0,0,0)))
year = b.tm_year-a.tm_year
month = b.tm_mon-mont.tm_mon
day = b.tm_mday-mont.tm_mday
if month<0:
	year-=1
	month=12+month
print("Your age is %d years %d months %d days"%(year,month,day))
