class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        # Build s1_freq and initial window of s2
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        left = 0
        right = len(s1)  # next character to add

        while right < len(s2):
            if s1_freq == s2_freq:
                return True
            s2_freq[ord(s2[right]) - ord('a')] += 1  # add new right
            s2_freq[ord(s2[left]) - ord('a')] -= 1   # remove old left
            left += 1
            right += 1

        return s1_freq == s2_freq  # check last window!

# Time Complexity: O(n)
# Space Complexity: O(1)