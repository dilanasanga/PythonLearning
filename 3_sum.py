class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = set()

        for i in range(len(nums)-2):
            firstNum = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                secondNum = nums[j]
                thirdNum = nums[k]
                poentialSum = firstNum + secondNum + thirdNum
                print(poentialSum, firstNum, secondNum, thirdNum)
                if poentialSum < 0:
                    j = j+1
                elif poentialSum >0:
                    k = k-1
                else:
                    triplets.add((firstNum, secondNum, thirdNum))
                    j = j+1 
                    k = k-1
                    while j < k and nums[j] == secondNum:
                        j = j+1
                    while j <k and nums[k] == thirdNum:
                        k = k-1
        return triplets

NumberList= [-1,5,1,8,5,4,0,-2,6,9] 
#NumberList= [5,-1,4,-3,0,6,-2,4,1,-1]   
newThreeSome= Solution()
out = newThreeSome.threeSum(NumberList) 
print(out)