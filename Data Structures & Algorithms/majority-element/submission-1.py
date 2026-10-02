class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore Voting algorithm
        candidate = None
        count = 0

        for num in nums:
            if count == 0: # If no vote change the candidate
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate