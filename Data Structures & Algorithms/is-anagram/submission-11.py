from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for ch in s:
            map_s[ch] += 1
        
        for ch in t:
            map_t[ch] += 1
        
        for key, value in map_s.items():
            if map_s[key] != map_t[key]:
                return False
        
        return True