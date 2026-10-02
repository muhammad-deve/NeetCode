from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        result = []

        for word in strs:
            freq_arr = [0] * 26
            for ch in word:
                freq_arr[ord(ch) - ord('a')] += 1
            
            freq_map[tuple(freq_arr)].append(word)

        
        return list(freq_map.values())
