class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        # Water amount = distance * lowest numbers

        for i in range(len(heights)):
            distance = 0
            for j in range(i + 1, len(heights)):
                distance += 1
                minimum = min(heights[i], heights[j])
                if result < minimum * distance:
                    result = minimum * distance
        
        return result