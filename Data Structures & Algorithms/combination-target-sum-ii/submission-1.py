class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, stack = [], []
        candidates.sort()

        def backtrack(i, current_sum) -> None:
            if current_sum == target:
                result.append(stack.copy())
                return
            
            if i == len(candidates) or current_sum > target:
                return
            
            stack.append(candidates[i])
            backtrack(i + 1, current_sum + candidates[i])
            stack.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, current_sum)

        backtrack(0, 0)
        return result