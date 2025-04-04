x = int(input("Insert Number: "))
if x < 0:
	x = -x
res = 0
while x > 0:
	res = res*10
#	print("old", res)
	res = res + x%10
	print("new", res)
	x = x//10
	
print(res)
