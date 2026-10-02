from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1
        
        for value in nums_map.values():
            if value > 1:
                return True
        
        return False