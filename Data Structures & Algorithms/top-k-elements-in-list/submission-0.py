from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        frequency_dict = defaultdict(int)
        for num in nums:
            frequency_dict[num] += 1

        # Step 2: Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put numbers into their frequency bucket
        for num, freq in frequency_dict.items():
            buckets[freq].append(num)

        # Step 4: Traverse from highest frequency to lowest
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result