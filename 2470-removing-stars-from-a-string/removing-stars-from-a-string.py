class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for n in s:

            if n != "*" :
                stack.append(n)
            else:
                stack.pop()

        return "".join(stack)

