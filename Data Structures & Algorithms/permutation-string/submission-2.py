class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        
        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1
        
        left, right = 0, 0  # ← fix: right should start at 0, not len(s2)-1
        while right < len(s2):
            # 1. Expand window: add s2[right] to frequency count
            s2_freq[ord(s2[right]) - ord('a')] += 1
            right += 1
            
            # 2. When window reaches target size, check for match
            if right - left == len(s1):
                if s1_freq == s2_freq:
                    return True
                
                # 3. Slide window: remove leftmost character
                s2_freq[ord(s2[left]) - ord('a')] -= 1
                left += 1
        
        return False