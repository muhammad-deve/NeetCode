class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ('+', '-', '/', '*')
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                match token:
                    case "+":
                        c = b + a
                    case "-":
                        c = b - a
                    case "*":
                        c = b * a
                    case "/":
                        c = int(b / a)
                
                stack.append(c)
        
        return int(stack[-1])