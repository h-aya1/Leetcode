class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []
        
        for n in logs:

            if n == "../" and stack:
                stack.pop()

            elif n == './':
                pass

            elif n == '../' and not stack:
                pass
                
            else:
                stack.append(n)
    

        return len(stack)