class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We will use freq lists or hash map to determine if it is anogram or not
        
        if len(s) != len(t):
            return False
        
        freq_s = [0] * 26
        freq_t = [0] * 26

        for ch in s:
            freq_s[ord(ch) - ord('a')] += 1
        
        for ch in t:
            freq_t[ord(ch) - ord('a')] += 1
        
        return freq_s == freq_t