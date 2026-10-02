class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        HASHMAP ===> KEY = FREQUENCY AND VALUES = THE NUMBER ITSELF
        ARRAY ===> index will be elemt's frequency
        """

        freq_map = {}
        freq_array = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
                freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
                freq_array[freq].append(num)
        
        for i in range(len(freq_array) - 1, 0, -1):
                for j in freq_array[i]:
                        result.append(j)
                if k == len(result):
                        return result