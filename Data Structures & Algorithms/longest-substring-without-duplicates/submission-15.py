class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If it is SLIDING WINDOW algorithm, both indexes start from 0's index
        left, right = 0, 0
        char_set = set()
        res = 0
        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            res = max(res, len(char_set))
            right += 1
        
        return res