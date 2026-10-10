class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i) -> None:
            # Correct Case
            if i == len(nums):
                result.append(stack.copy())
                return
            
            # Take ALL NODES
            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()

            # SKIP ALL THE NODES
            backtrack(i + 1)

        backtrack(0)
        return result