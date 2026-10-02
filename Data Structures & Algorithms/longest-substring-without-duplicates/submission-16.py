class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = set()
        res = 0

        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            res = max(res, len(window))
            right += 1
        
        return res