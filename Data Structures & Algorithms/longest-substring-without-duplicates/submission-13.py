class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            left, right = 0, 0
            result = 0
            char_set = set()

            while right < len(s):
                # If the coming character is exssit in the SET. SHRINK IT
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                
                char_set.add(s[right])
                result = max(result, len(char_set))
                right += 1
            
            return result
        