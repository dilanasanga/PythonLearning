def arithmatic(input1,input2):
    output1 = int(input1) + int(input2)
    output2 = int(input1) - int(input2)
    output3 = int(input1) * int(input2)
    output4 = int(input1) / int(input2)

    print(" sum= ", output1, "\n", "substract= ", output2,"\n",  "multiply= ", output3,"\n",  "divission= ", output4)

input_values = input()
inputnumbers = input_values.split()
arithmatic(inputnumbers[0],inputnumbers[1])

