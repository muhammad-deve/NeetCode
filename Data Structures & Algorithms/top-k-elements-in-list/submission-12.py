class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Store NUMBER as KEY and Frequency as Value
        # Store frequecy as INDEX and element(s) as element of that index
        freq_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for number, count in freq_map.items():
            freq_list[count].append(number)
        
        for i in range(len(freq_list) - 1, 0, -1):
            for n in freq_list[i]:
                result.append(n)
            if k == len(result):
                return result