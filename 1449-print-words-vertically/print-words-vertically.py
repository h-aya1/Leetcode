class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        ans = []
        maxL = 0
        for word in s:
            maxL = max(maxL , len(word))
        for i in range(maxL):
            st = ""
            for word in s:
                if i < len(word):
                    st += word[i]
                else:
                    st += " "
            ans.append(st.rstrip())
        return ans 