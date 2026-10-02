class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0

        for index, element in enumerate(nums):
            length = 0

            while (element + length) in nums_set and (element - 1) not in nums_set:
                length += 1
            
            result = max(result, length)

        return result