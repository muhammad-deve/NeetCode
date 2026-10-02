class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left, right = 0, 0
        result = 0

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            current_length = len(char_set)
            result = max(current_length, result)
            right += 1
        
        return result

