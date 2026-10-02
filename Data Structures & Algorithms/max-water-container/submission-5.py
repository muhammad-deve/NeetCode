class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = distance * min(heights[left], [right])
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            distance = right - left
            area = min(heights[right], heights[left]) * distance
            maxArea = max(area, maxArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea