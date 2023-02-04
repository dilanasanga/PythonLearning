#Write your code below this line 👇
print ("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip = input("What presentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_int = int(tip)
people_int = int(people)

personal_cost = (total_bill_float * (tip_int+100)/100)/people_int
round_personal_cost = round (personal_cost,2)
print (f"each person should pay: ${round_personal_cost}")
