class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set(nums)

        return len(numbers) != len(nums)