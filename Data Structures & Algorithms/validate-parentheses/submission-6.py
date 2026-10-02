class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in bracket_map.keys() and len(stack) != 0 and stack[-1] == bracket_map[i]:
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0