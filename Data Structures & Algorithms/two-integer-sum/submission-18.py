from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)

        for index, num in enumerate(nums):
            nums_map[num] = index
        
        for index, num in enumerate(nums):
            output = target - num
            if output in nums_map and nums_map[output] != index:
                return [min(nums_map[output], index), max(nums_map[output], index)]