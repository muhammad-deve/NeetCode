from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for index, num in enumerate(nums):
            wanted = target - num

            if wanted in hash_map:
                return [hash_map[wanted], index]
            
            hash_map[num] = index