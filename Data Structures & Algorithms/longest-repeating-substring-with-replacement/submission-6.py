class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result = 0, 0, 0
        counts = [0] * 26 # There is 26 letters in the Alphabet
        max_freq = 0

        while right < len(s):
            counts[ord(s[right]) - 65] += 1
            max_freq = max(max_freq, counts[ord(s[right]) - 65])
            # If the WINDOW is invalid!
            while ((right - left) + 1) - max_freq > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1
            # If the WINDOW is valid!
            result = max(result, ((right - left) + 1))
            right += 1

        return result