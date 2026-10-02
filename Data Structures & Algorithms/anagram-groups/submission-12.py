from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for word in strs:
            array = [0] * 26
            for ch in word:
                array[ord(ch) - ord('a')] += 1
            
            hash_map[tuple(array)].append(word)
        
        return list(hash_map.values())

        