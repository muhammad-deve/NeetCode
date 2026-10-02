class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                # Pop two operands (order matters!)
                b = stack.pop()  # second operand
                a = stack.pop()  # first operand
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # '/'
                    result = int(a / b)  # truncate toward zero
                
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]