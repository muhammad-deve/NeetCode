from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Having only lowercase letters is a HINT
        # Element is the frequecny and index represetn the LETTER
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        for index, character in enumerate(s1):
            freq_s1[ord(character) - ord('a')] += 1
        
        left, right = 0, 0
        while right < len(s2):
            freq_s2[ord(s2[right]) - ord('a')] += 1
            length = (right - left) + 1
            
            if length == len(s1):
                if freq_s1 == freq_s2:
                    return True
                freq_s2[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            right += 1
        
        return False
            

            
        


        

        

