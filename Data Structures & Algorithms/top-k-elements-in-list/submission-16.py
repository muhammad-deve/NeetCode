from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        freq_list = [[] for _ in range(len(nums) + 1)]
        result = []
        
        for num in nums:
            hash_map[num] += 1
        
        """
        3: 89
        4: 45
        42: 465
        2: 29
    
        """
        for key, value in hash_map.items():
            freq_list[value].append(key)

        for i in range(len(freq_list) - 1, 0, -1):
            for j in freq_list[i]:
                result.append(j)
                if len(result) == k:
                    return result
