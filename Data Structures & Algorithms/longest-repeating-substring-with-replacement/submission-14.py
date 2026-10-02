class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0
        freq_array = [0] * 26

        while right < len(s):
            freq_array[ord(s[right]) - ord('A')] += 1

            if (right - left) + 1 - max(freq_array) > k:
                freq_array[ord(s[left]) - ord('A')] -= 1
                left += 1
            else:
                res = max(res, (right - left) + 1)
            
            right += 1
        
        return res