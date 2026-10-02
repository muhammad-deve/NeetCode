class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for i in range(len(s)):
            if (i + 1) > 0 and s[i] in brackets.keys() and len(stack) > 0 and stack[-1] == brackets[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack) == 0