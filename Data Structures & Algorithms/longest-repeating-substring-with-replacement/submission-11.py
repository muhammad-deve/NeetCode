class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        result = 0
        counts = [0] * 26

        while right < len(s):
            counts[ord(s[right]) - ord('A')] += 1
            
            if ((right - left) + 1) - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            else:
                result = max(result, (right - left) + 1)
            
            right += 1
            
        return result