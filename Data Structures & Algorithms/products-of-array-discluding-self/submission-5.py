class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix, suffix = 1, 1

        # Prefix products
        for i in range(len(nums)):
                result[i] = prefix
                prefix = prefix * nums[i]
        
        # Sufix products
        for i in range(len(nums) - 1, -1, -1):
                result[i] *= suffix
                suffix = suffix * nums[i]
        
        return result