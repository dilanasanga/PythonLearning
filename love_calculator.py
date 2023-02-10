# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

full_string = name1+name2
full_string_lowercase = full_string.lower()
letter_t = full_string_lowercase.count("t")
letter_r = full_string_lowercase.count("r")
letter_u = full_string_lowercase.count("u")
letter_e = full_string_lowercase.count("e")

true_count = letter_t + letter_r + letter_u + letter_e

letter_l = full_string_lowercase.count("l")
letter_o = full_string_lowercase.count("o")
letter_v = full_string_lowercase.count("v")
letter_e = full_string_lowercase.count("e")

love_count = letter_l + letter_o + letter_v + letter_e

total_count = str(true_count) + str(love_count)

if int(total_count)<10 or int(total_count) > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif int(total_count) >=40 and int(total_count) <= 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")

