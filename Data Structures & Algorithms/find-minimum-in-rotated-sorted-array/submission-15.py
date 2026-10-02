class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        If it is moved, the MIN will be in UNSORTED portion of the ARRAY
        """

        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            # If it is ALREADY SORTED return min
            if nums[left] <= nums[right]:
                result = min(result, nums[left])
                break
            
            mid = (left + right) // 2
            # result = min(result, nums[mid])

            # If it is ROTATED
            if nums[left] <= nums[mid]: # It means this LEFT side is SORTED and the MIN is in RIGHT portion
                left = mid + 1
            elif nums[left] > nums[mid]: # It means LEFT side is UNSORTED and MIN is in LEFT portion
                right = mid
        
        return result
