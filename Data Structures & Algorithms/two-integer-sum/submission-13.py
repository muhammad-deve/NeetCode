class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, element in enumerate(nums):
            compliment = target - element

            if compliment in seen:
                return [seen[compliment], index]
            else:
                seen[element] = index
            
        
