class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            potential_result = numbers[left] + numbers[right]
            if potential_result < target:
                left += 1
            elif potential_result > target:
                right -= 1
            else:
                return [left + 1, right + 1]