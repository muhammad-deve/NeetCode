class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # If SLIDING WINDOW algorithm both pointes starts from 0's index
        # Saying it is only UPPERCASE LETTERS it measn i will use "ord()"
        left, right = 0, 0
        freq_list = [0] * 26
        res = 0
        
        while right < len(s):
            freq_list[ord(s[right]) - ord('A')] += 1
            # It means this WINDOW is INVALID
            if (right - left) + 1 - max(freq_list) > k:
                freq_list[ord(s[left]) - ord('A')] -= 1
                left += 1
            else:
                res = max(res, (right - left) + 1)
            right += 1
        return res
