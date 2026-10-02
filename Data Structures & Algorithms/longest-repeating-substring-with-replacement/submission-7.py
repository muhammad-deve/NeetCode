class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result = 0, 0, 0
        counts = [0] * 26

        while right < len(s):
            counts[ord(s[right]) - ord('A')] += 1
            # If the window is invalid (If the number of changes we have to make is greater than we can change)
            while ((right - left) + 1) - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            result = max(result, (right - left) + 1)
            right += 1

        return result
        