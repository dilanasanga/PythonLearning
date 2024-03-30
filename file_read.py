# with open('test.txt','r') as file1:
#     content = file1.readline(6)
#     print(content)
#     print("content printed")
#     print(type(content))
# #    print(file1.closed)
#     for line in content:
#         print(line)
# #    for line in file1:
#  #       print(line)

# print(file1.closed)

file2 = open("test.txt", "r")
print(file2)
#content = file2.read()
content2 = file2.readline()

#print(content)
print(content2)
# print(file2.name)
# for content in file2:
#     print(content)
# file2.close()

with open("test.txt","r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", i, ": ", line)
            i = i + 1

