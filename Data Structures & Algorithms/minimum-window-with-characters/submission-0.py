from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = defaultdict(int), defaultdict(int)
        result, resultLen = [-1, -1], float("inf")
        
        for ch in t:
            countT[ch] += 1

        have, need = 0, len(countT)

        left, right = 0, 0        # ← was missing right = 0
        while right < len(s):
            window[s[right]] += 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            
            while have == need:
                # Update our result
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = (right - left) + 1
                
                # Pop from the left
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            right += 1

        l, r = result
        return s[l:r + 1] if resultLen != float("inf") else ""