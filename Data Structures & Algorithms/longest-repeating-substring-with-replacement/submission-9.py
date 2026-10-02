class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        result = 0
        counts = [0] * 26

        while right < len(s):
            counts[ord(s[right]) - ord('A')] += 1
            # WINDOW is invalid if the number of changes we have to make is greater than the number of changes we can make
            # SHRINK the WINDOW
            if (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            else:
                result = max(result, (right - left) + 1)
            right += 1
        
        return result
        