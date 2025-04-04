def duplicates(num):
	seen = set()
	duplicate = set()
	for number in num:
		if number in seen:
			duplicate.add(number)
		else:
			seen.add(number)
	return list(duplicate)

num = [4,2,6,1,1,5,4,6,8,0]
print ("Duplicaes are", duplicates(num))
