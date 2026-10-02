class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i, current_sum) -> None:
            if current_sum == target:
                result.append(stack.copy())
                return
            
            if i == len(nums) or current_sum > target:
                return
            
            backtrack(i + 1, current_sum)

            stack.append(nums[i])
            backtrack(i, nums[i] + current_sum)
            stack.pop()
        
        backtrack(0, 0)
        return result
