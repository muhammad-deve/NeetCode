class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for c in s:
            if c in bracket_map:  # If it's a closing bracket
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != bracket_map[c]:
                    return False
                stack.pop()  # Remove the matched opening bracket
            else:  # It's an opening bracket
                stack.append(c)
        
        # Valid if stack is empty (all brackets matched)
        return len(stack) == 0