class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)

        for index, element in enumerate(nums):
            
            # Check if the element is begenning of the SEQUENCE
            if (element - 1) not in nums_set:
                length = 0

                while (element + length) in nums_set and index < len(nums):
                    length += 1
                
                result = max(length, result)

        return result