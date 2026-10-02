class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = distance * min(element1, elemnt2)
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left <= right:
            distance = right - left
            area = distance * min(heights[left], heights[right])
            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

            
