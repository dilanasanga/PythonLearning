#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        xoriginal = x
        x1 = abs(x)
        finalstring = ''
        y = []
        for i in range(len(str(x1))):
            out = x1%10
            x1 = x1//10
#            out, x1 = divmod(x1, 10)
            y.append(out)
        finalstring = ''.join(map(str,y))
        finalint = int(finalstring)
        if finalint < 2**31-1 and finalint > -2**31:
            if x < 0:
                return(0-finalint)
            else:
                return(finalint)
        else:
            return(0)
b = int(input("Insert Number: "))
a = Solution()
print(a.reverse(b))