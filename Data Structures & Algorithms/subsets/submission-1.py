class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i) -> None:
            if i == len(nums):
                result.append(stack.copy())
                return
            
            backtrack(i + 1)

            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()
        
        backtrack(0)
        return result
        
