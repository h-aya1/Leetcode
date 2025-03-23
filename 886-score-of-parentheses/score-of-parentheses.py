class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]

        for par in s:
            
            if par == "(":
                stack.append(0)

            else:

                top = stack.pop()

                if top == 0:
                    stack[-1] += 1 
                else:
                    stack[-1] += 2 * top

        return stack[0]
