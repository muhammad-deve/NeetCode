class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(['+', '-', '*', '/'])
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

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
        
        return stack[0]


