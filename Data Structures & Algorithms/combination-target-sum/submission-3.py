class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i, current_sum) -> None:
            if current_sum == target:
                result.append(stack.copy())
                return
            
            if current_sum > target or i == len(nums):
                return
            
            # Take the NODE
            stack.append(nums[i])
            backtrack(i, current_sum + nums[i]) 
            stack.pop()

            # Do not take the NODE
            backtrack(i + 1, current_sum)   

        backtrack(0, 0)
        return result