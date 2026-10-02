class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_array = [0] * 26
        s2_array = [0] * 26

        for ch in s1:
            s1_array[ord(ch) - ord('a')] += 1
        
        left, right = 0, 0
        while right < len(s2):
            s2_array[ord(s2[right]) - ord('a')] += 1

            length = (right - left) + 1

            if len(s1) == length:
                if s1_array == s2_array:
                    return True
                s2_array[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            right += 1
        
        return False
                
