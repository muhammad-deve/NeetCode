class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        BINARY SEARCH for O(logn)
        If ARRAY is SORTED and ROTATED, we can devide that ARRAY into two PORTIONS! SORTED and UNSORTED
        MIN value is going to be always in UNSORTED PORTIONS
        Because the MIN will be always one index after MAX value
        """

        left, right = 0, len(nums) - 1
        result = nums[0]
        # Do not worry about whether to put '=' or not! It will be clear in the END
        while left <= right:
            # If array is already SORTED save left value as potential RESULT
            if nums[left] <= nums[right]:
                result = min(result, nums[left])
                break
            
            # Mid value can be also MIN that's why save it as potential RESULT as well
            mid = (left + right) // 2
            result = min(result, nums[mid])

            # Find which PORTION is UNSORTED!
            if nums[left] <= nums[mid]: # Left portion is SORTED
                left = mid + 1
            else: # Left portion is UNSORTED
                right = mid - 1
        
        return result


            
