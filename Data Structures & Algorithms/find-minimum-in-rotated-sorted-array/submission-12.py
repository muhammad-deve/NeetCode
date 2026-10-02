class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = nums[0]
        
        while left <= right:
            # If this portion is already sorted, leftmost is the min
            if nums[left] <= nums[right]:
                result = min(nums[left], result)
                break  # We found the min in this portion
            
            mid = (left + right) // 2
            result = min(nums[mid], result)  # Track minimum
            
            # If LEFT portion is sorted, min must be in RIGHT
            if nums[left] <= nums[mid]:
                left = mid + 1  # Search right (unsorted portion)
            # If RIGHT portion is sorted, min must be in LEFT
            else:
                right = mid - 1  # Search left (unsorted portion)
        
        return result