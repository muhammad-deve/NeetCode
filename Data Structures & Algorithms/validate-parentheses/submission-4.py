class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in bracket_map.keys() and len(stack) != 0 and stack[-1] == bracket_map[c]:
                stack.pop()

            else:
                stack.append(c)
        
        return len(stack) == 0