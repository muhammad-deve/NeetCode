from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_hash = defaultdict(int)

        for i in range(len(nums)):
            nums_hash[nums[i]] = i

        for index, num in enumerate(nums):
            if target - num in nums_hash and index != nums_hash[target - num]:
                return [min(index, nums_hash[target - num]), max(index, nums_hash[target - num])]
            
        