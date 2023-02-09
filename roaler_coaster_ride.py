# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
height = int(input("Insert your height: "))
if height > 120:
    print("You cant ride")
    age = int(input("insert your age: "))
    if age < 12:
        charge = 12
    elif age >= 18:
        charge = 12
    else:
        charge = 7
    want_photos = input("Do you need to take a photo?Y/N : ")
    if want_photos == "Y":
        charge +=3
    print(f"Your total bill is {charge}")
else:
    print("Sorry, you do not have the height")
