class Solution(object):
#    def reverse(self, x):
    def reverse(self, x):
#check whwther the number is negative or possitive:
        if int(x) < 0:
            negative_possitive = -1
        else:
            negative_possitive = 1
        x1 = abs(int(x))
        reverse_value = int(str(x1)[::-1]) * negative_possitive

        if reverse_value < -2**31 or reverse_value > 2**31 -1:
            return 0
        return reverse_value

#inputnumber = input("inser a value:")
#print(reverse(inputnumber))