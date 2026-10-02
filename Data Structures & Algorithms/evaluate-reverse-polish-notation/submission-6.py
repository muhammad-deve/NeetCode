class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ('+', '-', '*', '/')

        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()

                match i:
                    case '+':
                        c = b + a
                    case '-':
                        c = b - a
                    case '*':
                        c = b * a
                    case '/':
                        c = int(b / a)
                stack.append(c)
        
        return int(stack[0])