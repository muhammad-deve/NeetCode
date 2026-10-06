class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, stack = [], []
        candidates.sort()

        def backtrack(i, current_sum) -> None:
            if current_sum == target:
                result.append(stack.copy())
                return
            
            if current_sum > target or i == len(candidates):
                return
            
            # Take the NODE:
            stack.append(candidates[i])
            backtrack(i + 1, current_sum + candidates[i])
            stack.pop()

            # SKip duplicates   
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            # Do not take the NODE
            backtrack(i + 1, current_sum) 

        backtrack(0, 0)
        return result