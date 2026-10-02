class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
                left, right = 0, 0 
                new_string = set()
                result = 0

                while right < len(s):
                    while s[right] in new_string:
                        new_string.remove(s[left])
                        left += 1
                    
                    new_string.add(s[right])
                    result = max(result, len(new_string))
                    right += 1
                
                return result