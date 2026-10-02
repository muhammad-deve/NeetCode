class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            distance = (right - left)
            area = distance * min(heights[left], heights[right])

            if heights[left] < heights[right]:
                left += 1
            else:
                heights[left] > heights[right]
                right -= 1

            result = max(result, area)
        
        return result