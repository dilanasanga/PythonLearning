class Solution(object):
    def isPalindrome(self, x):
        reverse = x[::-1]
        if reverse == x:
            return True
        else:
            return False
        
new_Solution = Solution()
new_Solution.isPalindrome('121')

# class Solution(object):
#     def isPalindrome(self, x):
#         reverse = 0
#         while x > 0:
#             remainder = x%10
#             quotient = x//10
#             x = quotient
#             reverse = reverse * 10 + x % 10
#         if reverse == x:
#             return True
#         else:
#             return False