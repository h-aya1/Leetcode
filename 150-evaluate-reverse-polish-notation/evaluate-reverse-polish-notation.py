class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:

            if n == '+':

                a = int(stack.pop())
                b = int(stack.pop())
                c = b + a
                stack.append(c)

            elif n == '-':

                a = int(stack.pop())
                b = int(stack.pop())
                c = b - a
                stack.append(c)

            elif n == '*':

                a = int(stack.pop())
                b = int(stack.pop())
                c = b * a
                stack.append(c)

            elif n == '/':

                a = int(stack.pop())
                b = int(stack.pop())
                c = int(b / a)
                stack.append(c)

            else:

                stack.append(n)
          
    

        return int(stack.pop())