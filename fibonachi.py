terms=int(input("what is the nth term you need: "))
first_vallue = 0
seconf_value = 1
count = 0

if terms<=0:
  print (f"the value you enstered is {terms}, please insert a positive integer")
elif terms==1:
  print(f"Fibonachi sequence upto {terms} is:")
  print(first_vallue)
else:
  while count < terms:
    print(first_vallue)
    nth=first_vallue+seconf_value
    first_vallue = seconf_value
    seconf_value = nth
    count = count +1




terms=int(input("what is the nth term you need: "))
n1 = 0
n2 = 1
count = 0

if terms <=0:
  print (f"the value you enstered is {terms}, please insert a positive integer")
elif terms==1:
  print(f"Fibonachi sequence upto {terms} is:")
else:
  while count < terms:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1
