class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            if min(height[left], height[right]) * (right-left) > max_area:
                max_area = (right-left)*min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            elif height[right] < height [left]:
                right -= 1
            else: 
                left += 1
                right -= 1
        return max_area
