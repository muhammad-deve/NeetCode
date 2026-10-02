class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # This is O(1) Space complexity!!
        # Because length of these arrays are not proporsional to s or t
        s_freq = [0] * 26
        t_freq = [0] * 26

        for ch in s:
            s_freq[ord(ch) - ord('a')] += 1
        
        for ch in t:
            t_freq[ord(ch) - ord('a')] += 1
        
        return s_freq == t_freq