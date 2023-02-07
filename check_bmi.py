# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/height**2
round_BMI = round(BMI)
if round_BMI < 18.5:
    print(f"Your BMI is {round_BMI}, you are underweight.")
elif round_BMI < 25:
    print(f"Your BMI is {round_BMI}, you have a normal weight.")
elif round_BMI < 28:
    print(f"Your BMI is {round_BMI}, you are slightly overweight")
elif round_BMI < 33:
    print(f"Your BMI is {round_BMI}, you are obese")
else:
    print(f"Your BMI is {round_BMI}, you are clinically obese.")
