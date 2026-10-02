class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We are going to use two pointers approach
        left, right = 0, len(heights) - 1
        result = 0

        while left <= right:
            distance = right - left
            amount = distance * min(heights[left], heights[right])
            result = max(amount, result)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result
            
