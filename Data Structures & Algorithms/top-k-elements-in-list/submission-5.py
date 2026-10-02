from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        freq_list = [[]for _ in range (len(nums) + 1)]
        result = []

        # Make the freq_dict
        for i in nums:
            freq_dict[i] += 1
        
        # Make the freq_list
        for key, value in freq_dict.items():
            freq_list[value].append(key)
        
        # Extract the final result
        for i in range(len(nums), 0, -1):
            for j in freq_list[i]:
                result.append(j)
                if len(result) == k:
                    return result

    