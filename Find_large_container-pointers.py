class Solution(object):
    def maxArea(self, height):
        low_height = 0
        area = 0
        i = 0
        j = len(height) -1
        #print(j)
        while j > i:
            if height[i] > height[j]:
                low_height = height[j]
            else:
                low_height = height[i]
            max_area = low_height * (j-i)
            if max_area > area:
                area = max_area
                #print(max_area)
                #print(area)
            if height[i] < height[j]:
                i+=1
            else:
                j -=1
        return area

#height = [1,8,6,2,5,4,8,3,7]
height = [2,3,4,5,18,17,6]
new_Solution =Solution()
area = new_Solution.maxArea(height)
print(area)

