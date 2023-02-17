
squire=0
highest_value=0
#input=input("insert the number")
for numbers in range(0,100):
  squire=numbers**2
  print(f"number is: {numbers}, squire is: {squire}")
  sum = 0
  for digits in str(squire):
    sum = sum + int(digits)
  print(f"sum={sum}")
  if sum>highest_value:
    highest_value=sum
    r=numbers
    
print(f"highest value {highest_value}")
print(f"r {r}")

