class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []

        for i in nums:
            if i in numbers:
                return True
            numbers.append(i)
        return False