from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        return max(freq_dict, key=freq_dict.get)