class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i, current_sum) -> None:
            if current_sum == target:
                result.append(stack.copy())
                return
            
            if current_sum > target or i == len(nums):
                return
            
            backtrack(i + 1, current_sum)

            stack.append(nums[i])
            backtrack(i, current_sum + nums[i])
            stack.pop()
        
        backtrack(0, 0)
        return result