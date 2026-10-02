class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, right = 0, 0
        result = 0

        while right < len(s):
            # Remove duplicates from left
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            result = max(result, right - left + 1)
            right += 1
        
        return result
        
        # Time: O(n) - each character added/removed at most once
        # Space: O(min(n, m)) - m is charset size