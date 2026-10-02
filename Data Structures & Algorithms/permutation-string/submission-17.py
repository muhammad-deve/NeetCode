class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1
        
        left, right = 0, 0
        while right < len(s2):
            s2_freq[ord(s2[right]) - ord('a')] += 1

            if (right - left) + 1 == len(s1):
                if s1_freq == s2_freq:
                    return True
                else:
                    s2_freq[ord(s2[left]) - ord('a')] -= 1
                    left += 1
            
            right += 1
        
        return False