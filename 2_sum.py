sum = 10
list = [2,4,6,7,3,8]

def two_sum(list,sum):
	seen = {}
	for i in range(len(list)):
		diff = sum - list[i]
		if diff in seen:
			return[seen[diff], i]
		else:
			seen[list[i]] = i
			print(seen)

print(two_sum(list,sum))