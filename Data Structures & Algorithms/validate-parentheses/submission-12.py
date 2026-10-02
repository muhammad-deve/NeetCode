class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for ch in s:
            if ch in brackets.keys() and len(stack) != 0 and stack[-1] == brackets[ch]:
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0