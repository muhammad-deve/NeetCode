class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        
        for i in range(len(heights)):
            min_height = heights[i]
            
            for j in range(i, len(heights)):
                # Update minimum height in the range [i, j]
                min_height = min(min_height, heights[j])
                
                # Calculate area with this range
                width = j - i + 1
                area = width * min_height
                result = max(result, area)
        
        return result