class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Will be using HashMap where i store indexes as values and num as keys
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
        
        