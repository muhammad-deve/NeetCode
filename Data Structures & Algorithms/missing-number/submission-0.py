class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = sum(nums)
        wanted_sum = 0

        for i in range(n + 1):
            wanted_sum += i
        
        return wanted_sum - actual_sum