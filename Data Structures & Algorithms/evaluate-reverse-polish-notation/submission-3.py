class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ('+', '-', '*', '/')

        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                match i:
                    case '+':
                        c = a + b
                    case '-':
                        c = a - b
                    case '*':
                        c = a * b
                    case '/':
                        c = int(a / b)
                stack.append(str(c))

        return int(stack[0])