class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'}': '{', ')': '(', ']': '['}
        stack = []

        for ch in s:
            if ch in bracket_map.keys() and len(stack) != 0 and stack[-1] == bracket_map[ch]:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0