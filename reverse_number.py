class solution(object):
    def reverse(self,x):
        negative = 1
        if x<1:
            x = -x
            negative= -1
        final = 0
        while x>0:
            remainder=x%10
            quotient=x//10
            x = quotient
            final= final*10 + remainder
        final = final * negative
        if final >= 2**31 -1 or final < -2**31:
            print (0)
        else:
            print(final)
new_solution = solution()
new_solution.reverse(467959428)
#out = new_solution.reverse(4551)
#print(out)