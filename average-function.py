#Define the function
def number_average(inputnumbers):
#Define the total variable    
    total = 0
#Loop through the list
    for i in inputnumbers: 
# What is the value for i
#Add the values in list to the total(convereted the string in list to an int)
        total = total + int(i)
#fidn the average
    average = total/int(len(inputnumbers))
    print(average)

#Input values
input_string = input()
#Input is split by spaces and
inputnumbers = input_string.split()
#Call function
number_average(inputnumbers)
