from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        frequency_list = [[] for _ in range(len(nums) + 1)]
        result = []
        
        # Step 1: building a frequency HashMap
        for i in nums:
            frequency_dict[i] += 1
        
        # Saving frequency_dict into frequency_list (where index defines frequency)
        for key, value in frequency_dict.items():
            frequency_list[value].append(key)

        # Extracting result data from frequency_list (from highest to lowest frequency)
        for i in range(len(nums), 0, -1):  # Changed range start to len(nums)
            for num in frequency_list[i]:   # Changed to iterate over frequency_list[i]
                result.append(num)
                if len(result) == k:         # Changed to len(result)
                    return result
    