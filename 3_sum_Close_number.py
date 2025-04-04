class Solution:
    def threeSumClose(self, nums: list[int], target: int ) -> int:
        nums.sort()
        total = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            sum = nums[i] + nums[j] + nums[k]
            print(nums[i], nums[j], nums[k])
            if sum == target:
                print(nums[i], nums[j], nums[k])
                return sum
            if abs(sum - target) < (total - target):
                total = sum
            if total < target:
                j = j+1
            elif total > target:
                k = k-1
            else:
                print(nums[i], nums[j], nums[k])
                return total
        print(nums[i], nums[j], nums[k])
        return total

            

list = [-1,5,1,8,5,4,0,-2,6,9]
newSulotion = Solution()
out = newSulotion.threeSumClose(list,0)
print(out)


