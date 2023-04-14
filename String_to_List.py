#list1 = [2,3,4,5,6,7,38]
#
#sum_list=0
#for j in range(len(list1)):
#	sum_list=(list1[j])+sum_list
#mean=sum_list/len(list1)
#print("Count is", len(list1))
#print("total  is", sum_list)
#print("mean is", round(mean,3))

string = "STRING"
j=0
s=''
characters = list(string)
print(characters)
j = len(characters)
print(j)
while j > 0:
	s=characters[j-1]+s
	j = j-1
print(s)


