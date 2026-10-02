from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for ch in s:
            hash_s[ch] += 1
        
        for ch in t:
            hash_t[ch] += 1
        
        return hash_s == hash_t