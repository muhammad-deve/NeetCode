class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i):
            if i == len(nums):
                result.append(stack.copy())
                return
            
            # We dont add
            backtrack(i + 1)


            # We add
            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()

        backtrack(0)
        return result