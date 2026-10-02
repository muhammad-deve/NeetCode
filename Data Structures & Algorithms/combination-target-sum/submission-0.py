class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, stack = [], []

        def backtrack(i, current_sum):
            if current_sum == target:
                result.append(stack.copy())
                return
            
            if i == len(nums) or current_sum > target:
                return
            
            # It is preetty uselss
            backtrack(i + 1, current_sum)
            
            # If 'current_sum' is smaller we shoudd increse it
            stack.append(nums[i])
            backtrack(i, current_sum + nums[i])
            stack.pop()
        
        backtrack(0, 0)
        return result