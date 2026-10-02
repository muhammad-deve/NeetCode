class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []

        left, right = 0, 0
        while right < len(nums):
            if (right - left) + 1 == k:
                window = nums[left:right + 1]
                results.append(max(window))
                left += 1
            
            right += 1
        
        return results
