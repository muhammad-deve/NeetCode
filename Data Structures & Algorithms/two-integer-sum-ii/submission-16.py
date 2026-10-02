class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted is the INFORMATION
        left, right = 0, len(numbers) - 1

        while left < right: # This seciotn will take care of left != right (it will ensure they being equal)
            output = numbers[left] + numbers[right]
            
            if output > target:
                right -= 1
            elif output < target:
                left += 1
            else:
                return [left + 1, right + 1]