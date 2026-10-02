class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0
        while left < right:
            distance = right - left
            area = distance * min(heights[left], heights[right])
            maxArea = max(maxArea, area)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea
            
