class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft, maxRight = 0, 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    result += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    result += maxRight - height[right]
                right -= 1

        return result