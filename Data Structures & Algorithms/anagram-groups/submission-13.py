from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for word in strs:
            freq_list = [0] * 26
            for ch in word:
                freq_list[ord(ch) - ord('a')] += 1
            
            freq_map[tuple(freq_list)].append(word)
        
        return list(freq_map.values())