class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            distance = right - left
            amount = distance * min(heights[left], heights[right])
            result = max(amount, result)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return result            
