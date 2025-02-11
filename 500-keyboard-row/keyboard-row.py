class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        ans = []
        for word in words:
            lword = set(word.lower())
            if lword <= r1 or lword <= r2 or lword <= r3:
                ans.append(word)
        return ans
            
                
