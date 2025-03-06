class Solution:
    def isValid(self, s: str) -> bool:

        valid = {'(' : ')' , '{' : '}' , '[' : ']'}

        st = []
        for sign in s:

            if sign in valid:
                st.append(sign)
            else:
                if not st:
                    return False

                if valid[st[-1]] != sign:
                    return False
                st.pop()
                
        return not st
