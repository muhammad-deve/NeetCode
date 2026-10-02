class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            just = numbers[left] + numbers[right]
            if just == target:
                return [left + 1, right + 1]
            elif just > target:
                right -= 1
            elif just < target:
                left += 1
        
            