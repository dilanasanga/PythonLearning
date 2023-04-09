list = [4,23,43,12,9,91,58,40,73,1,19,66]

for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)       