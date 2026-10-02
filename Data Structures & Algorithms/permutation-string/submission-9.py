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
            # EXPAND the WINDOW
            s2_freq[ord(s2[right]) - ord('a')] += 1

            # If the length are the same, check if they are permutation
            if len(s1) == (right - left) + 1:
                if s1_freq == s2_freq:
                    return True
                else:
                    # SHRINK THE WINDOW
                    s2_freq[ord(s2[left]) - ord('a')] -= 1
                    left += 1
            
            # No matter the condition incremnt right pointer
            right += 1
        
        return s1_freq == s2_freq