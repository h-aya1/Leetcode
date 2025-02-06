class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for st in words:
            for char in st:
                if char not in allowed:
                    ans -= 1
                    break
                
            ans += 1

        return ans