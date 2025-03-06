class Solution:
    def simplifyPath(self, path: str) -> str:

        s = path.split('/')
        stack  = []

        for dir in s:

            if dir == ".." :
                if stack:
                    stack.pop()
            elif dir != "" and dir != ".":
                stack.append(dir)


        return "/" + "/".join(stack)

                
