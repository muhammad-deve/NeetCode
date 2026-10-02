class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result = 0, 0, 0
        max_freq = 0
        freq_array = [0] * 26 # The number of letters

        while right < len(s):
            freq_array[ord(s[right]) - 65] += 1 # Index = letter, elemnt = frequency (65 to make it from 0)
            max_freq = max(max_freq, freq_array[ord(s[right]) - 65])
            
            while (right - left) + 1 - max_freq > k:
                freq_array[ord(s[left]) - 65] -= 1
                left += 1
            
            result = max(result, (right - left) + 1)
            right += 1

        return result

