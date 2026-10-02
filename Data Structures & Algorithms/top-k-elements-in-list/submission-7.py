from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        freq_list = [[]for _ in range(len(nums) + 1)]
        result = []

        # Step 1: Fill the freq_dict
        for i in range(len(nums)):
            freq_dict[nums[i]] += 1

        # Step 2: Fill the freq_list
        for key, value in freq_dict.items():
            freq_list[value].append(key)

        # Step 3: Extract the final result
        for i in range(len(nums), 0, -1):
            for j in freq_list[i]:
                result.append(j)
                if len(result) == k:
                    return result