from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        freq_array = [[] for _ in range(len(nums) + 1)]  # +1 to handle max frequency
        result = []

        # Step 1: Count frequencies
        for num in nums:
            freq_dict[num] += 1
        
        # Step 2: Put numbers into buckets by frequency
        for num, freq in freq_dict.items():
            freq_array[freq].append(num) 
        
        # Step 3: Collect top k frequent elements (iterate backwards)
        for i in range(len(freq_array) - 1, -1, -1):
            if freq_array[i]:
                result.extend(freq_array[i]) 
                if len(result) >= k:
                    break
        
        return result[:k]