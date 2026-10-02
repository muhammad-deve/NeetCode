from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        freq_list = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            freq_map[num] += 1
        
        for key, value in freq_map.items():
            freq_list[value].append(key)
        
        for i in range(len(freq_list) - 1, 0, -1):
            for j in freq_list[i]:
                result.append(j)

                if len(result) == k:
                    return result