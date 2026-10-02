class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            output = numbers[right] + numbers[left]

            if output > target:
                right -= 1
            elif output < target:
                left += 1
            else:
                return [left + 1, right + 1]