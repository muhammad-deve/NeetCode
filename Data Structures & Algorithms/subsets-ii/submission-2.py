class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, stack = [], []
        nums.sort()

        def backtrack(i) -> None:
            if i == len(nums):
                result.append(stack.copy())
                return
            
            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)
        return result