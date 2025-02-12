class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        #{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        
        for i , char in enumerate(s):
            last_idx[char] = i

        ans = []
        l = 0
        r = 0

        for i , char in enumerate(s):
            r = max(r,last_idx[char])

            if i == r:
                ans.append(r - l + 1)
                l = i + 1
        return ans
