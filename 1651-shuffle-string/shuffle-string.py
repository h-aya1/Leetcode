class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        ans = [0] * len(s)
        for i in range(len(s)):
            ans[indices[i]] = str(s[i])
        
        return "".join(ans)