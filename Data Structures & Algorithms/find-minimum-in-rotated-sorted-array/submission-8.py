class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The minimum value is going to be ALWAYS in te UNSORTED portion
        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            # If the array is already sorted return the smalles one
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            mid = (left + right) // 2
            result = min(nums[mid], result)

            # If LEFT portion is sorted
            if nums[left] <= nums[mid]:
                # Minimum is in the RIGHT portion
                left = mid + 1
            # If RIGHT portion is sorted
            else:
                # Minimum is in the LEFT portion
                right = mid - 1
        
        return result
            

