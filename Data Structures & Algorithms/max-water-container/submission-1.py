class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force
        result = 0
        for i in range(len(heights)):
            for j in range(1 + i, len(heights)):
                area = (j - i) * min(heights[i], heights[j]) # Minimum * distance
                result = max(area, result)

        return result