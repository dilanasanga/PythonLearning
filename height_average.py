
student_height = input("insert height comma separated: ").split(',')
print(f"student height list in string {student_height}")
for i in range(0,len(student_height)):
  student_height[i] = int(student_height[i])
print(f"student height list in ints {student_height}")

total_height=0
highest_height=0
total_student=0
for height in student_height:
  print(f"each height {height}")
  total_height=total_height+height
  total_student=total_student+1
  if height > highest_height:
    highest_height=height


average_height=round(total_height/total_student)
print(average_height)
print(highest_height)

total = 0
sum_upto = int(input("Upto which number you need sum: "))
for i in range (0,sum_upto+1):
  total =total+i

print(f"total= {total}")
