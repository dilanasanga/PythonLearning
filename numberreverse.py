#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

intmax = 2**31-1
intmin = -2**31
class Solution(object):
    def reverse(self, x):
        xoriginal = x
        x1 = abs(x)
        finalstring = ''
        y = []
        for i in range(len(str(x1))):
#            out = x1%10
#            x1 = x1//10
            out, x1 = divmod(x1, 10)
            y.append(out)
            print(y,xoriginal)
        finalstring = ''.join(map(str,y))
	finalint = int(finalstring)
	if {finalint < intmax || finalint > intmin}:
        	if x < 0:
            		return(0-finalint)
        	else:
            		return(finalint)
	else:
		return(0)
instance1 = (Solution(int(43222)))
instance1.Solution
